from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from foodOrdering.models import FoodOrders
from foodOrdering.serializers import FoodOrdersSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def orders_list(request):
    if request.method == 'GET':
        orders = FoodOrders.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            tutorials = orders.filter(title__icontains=title)
        
        orders_serializer = FoodOrdersSerializer(orders, many=True)
        return JsonResponse(orders_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        orders_data = JSONParser().parse(request)
        food_orders_serializer = FoodOrdersSerializer(data=orders_data)
        if food_orders_serializer.is_valid():
            food_orders_serializer.save()
            return JsonResponse(food_orders_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(food_orders_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = FoodOrders.objects.all().delete()
        return JsonResponse({'message': '{} Food Orders were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def orders_detail(request, pk):
    try: 
        orders = FoodOrders.objects.get(pk=pk) 
    except FoodOrders.DoesNotExist: 
        return JsonResponse({'message': 'The orders does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        food_orders_serializer = FoodOrdersSerializer(orders) 
        return JsonResponse(food_orders_serializer.data) 
 
    elif request.method == 'PUT': 
        orders_data = JSONParser().parse(request) 
        food_orders_serializer = FoodOrdersSerializer(orders, data=orders_data) 
        if food_orders_serializer.is_valid(): 
            food_orders_serializer.save() 
            return JsonResponse(food_orders_serializer.data) 
        return JsonResponse(food_orders_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        orders.delete() 
        return JsonResponse({'message': 'Order was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def orders_list_published(request):
    orders = FoodOrders.objects.filter(published=True)
        
    if request.method == 'GET': 
        orders_serializer = FoodOrdersSerializer(orders, many=True)
        return JsonResponse(orders_serializer.data, safe=False)