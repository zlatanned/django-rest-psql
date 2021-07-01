from rest_framework import serializers 
from foodOrdering.models import FoodOrders
 
 
class FoodOrdersSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = FoodOrders
        fields = ('id',
                  'title',
                  'description',
                  'published')