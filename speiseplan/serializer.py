from rest_framework import serializers, fields
from speiseplan.models import Catering, MealDate, Meal


class MealSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    price0 = serializers.CharField(max_length=64)
    price1 = serializers.CharField(max_length=64)

    class Meta:
        model = Meal
        fields = ('meals')


class MealDateSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=128)
    meals_of_mealdate = MealSerializer(many=True, read_only=True)

    class Meta:
        model = MealDate
        fields = ('text')


class CateringSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    mealdate = MealDateSerializer(many=True, read_only=True)
    
    class Meta:
        model = Catering
        fields = ('name')

