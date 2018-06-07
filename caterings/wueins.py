from django.db import models
from query.catering import CateringQuery
from query.mealdate import MealDateQuery
from query.meal import MealQuery
from speiseplan.models import Catering, MealDate, Meal
from speiseplan.serializer import CateringSerializer

class WUEins(models.Model):

    def __init__(self):
        self.catering_obj = None
        cq = CateringQuery(catering_id=0)
        result = cq.doQuery()
        if len(result):
            c = result[0]
            self.catering_obj = Catering.objects.create(name=c.name)
            dq = MealDateQuery(catering_id=c.id)
            for d in dq.doQuery():
                md_obj = MealDate.objects.create(catering=self.catering_obj, text=d.text)
                mq = MealQuery(catering_id=c.id, date_id=d.date_id)
                for m in mq.doQuery():
                    Meal.objects.create(catering=self.catering_obj, \
                                        mealdate=md_obj, \
                                        name=m.name, \
                                        price0=m.price0, \
                                        price1=m.price1)
        else:
            self.catering_obj = Catering.objects.create(name="Unknown catering")

    def serialized_data(self):
        return CateringSerializer(instance=self.catering_obj).data


