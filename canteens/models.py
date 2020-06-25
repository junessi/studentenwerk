from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

class Canteen(models.Model):
    name = models.CharField(max_length=255, default=0)
    fullname = models.CharField(max_length=255, default=0)
    address = models.CharField(max_length=255, default=0)
    city = models.CharField(max_length=255, default=0)
    detail = models.CharField(max_length=255, default=0)
    opentimes = models.CharField(max_length=255, default=0)
    contact = models.CharField(max_length=255, default=0)
    logourl = models.CharField(max_length=255, default=0)

    def __unicode__(self):
        return "{0}".format(self.name)


class MealDate(models.Model):
    date_id = models.IntegerField(default=19700101)
    canteen = models.ForeignKey(Canteen, related_name='mealdate', on_delete=models.CASCADE)
    text = models.CharField(max_length=128)

    def __str__(self):
        return "{0}".format(self.text)


class Meal(models.Model):
    canteen = models.ForeignKey(Canteen, related_name='meals_of_canteen', on_delete=models.CASCADE)
    mealdate = models.ForeignKey(MealDate, related_name='meals_of_mealdate', on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    price0 = models.CharField(max_length=32)
    price1 = models.CharField(max_length=32)

    def __str__(self):
        return "{0}: {1}/{2}".format(self.name, self.price0, self.price1)

