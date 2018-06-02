from django.db import models
from query.catering import CateringQuery
from query.mealdate import MealDateQuery
from query.meal import MealQuery
from speiseplan.models import Catering, MealDate, Meal
from speiseplan.serializer import CateringSerializer, MealDateSerializer, MealSerializer

class WUEins(models.Model):

    def __init__(self):
        self.catering_obj = None
        """
        cq = CateringQuery(catering_id=0)
        for c in cq.doQuery():
            c_obj = Catering(id=c.id, name=c.name)
            # c_obj.save()
            for d in c.mealdate:
                d_obj = MealDate(date_id=d.date_id, catering=c_obj, text=d.text)
                d_obj.save()
                print(d_obj)
                for m in d.meals:
                    m_obj = Meal(meal_id=m.meal_id, catering=c_obj, mealdate=d_obj, name=m.name, price0=m.price0, price1=m.price1)
                    m_obj.save()
                    print("    " + str(m_obj))

            self.catering_obj = c_obj
        """

        caterings = [{"id": 0, "name": "WUEins"},
                     {"id": 1, "name": "Alte Mensa"}]

    def serialized_data(self):
        return CateringSerializer(instance=self.catering_obj).data


