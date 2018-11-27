from django.db import models
from query.canteen import CanteenQuery
from query.mealdate import MealDateQuery
from query.meal import MealQuery
from speiseplan.models import Canteen, MealDate, Meal
from speiseplan.serializer import CanteenSerializer
import canteens.utils as utils

class WUEins(models.Model):

    def __init__(self, date_query = None):
        self.canteen_obj = None
        cq = CanteenQuery(canteen_id=0)
        result = cq.doQuery()
        if len(result):
            c = result[0]
            self.canteen_obj = Canteen.objects.create(name=c.name,
                                                      fullname=c.fullname,
                                                      address=c.address,
                                                      city=c.city,
                                                      detail=c.detail,
                                                      opentimes=c.opentimes,
                                                      contact=c.contact,
                                                      logourl=c.logourl)

            if date_query is not None:
                date_range_int = utils.parse_date(date_query)
                print(date_range_int)
                dq = MealDateQuery(canteen_id=c.id)
                for d in dq.doQuery(date_range_int):
                    md_obj = MealDate.objects.create(date_id=d.date_id, canteen=self.canteen_obj, text=d.text)
                    mq = MealQuery(canteen_id=c.id, date_id=d.date_id)
                    for m in mq.doQuery():
                        Meal.objects.create(canteen=self.canteen_obj, \
                                            mealdate=md_obj, \
                                            name=m.name, \
                                            price0=m.price0, \
                                            price1=m.price1)
        else:
            self.canteen_obj = Canteen.objects.create(name="Unknown canteen")

    def serialized_data(self):
        return CanteenSerializer(instance=self.canteen_obj).data

