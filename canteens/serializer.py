from rest_framework import serializers, fields
from canteens.models import Canteen, MealDate, Meal


class MealSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    price0 = serializers.CharField(max_length=64)
    price1 = serializers.CharField(max_length=64)

    class Meta:
        model = Meal
        fields = ('meals')


class MealDateSerializer(serializers.Serializer):
    date_id = serializers.IntegerField()
    text = serializers.CharField(max_length=128)
    meals_of_mealdate = MealSerializer(many=True, read_only=True)

    class Meta:
        model = MealDate
        fields = ('text')


class CanteenSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    fullname = serializers.CharField(max_length=255)
    address = serializers.CharField(max_length=255)
    city = serializers.CharField(max_length=255)
    detail = serializers.CharField(max_length=255)
    opentimes = serializers.CharField(max_length=255)
    contact = serializers.CharField(max_length=255)
    logourl = serializers.CharField(max_length=255)
    mealdate = MealDateSerializer(many=True, read_only=True)
    
    """
    class Meta:
        model = Canteen
        fields = ('name')
        """

