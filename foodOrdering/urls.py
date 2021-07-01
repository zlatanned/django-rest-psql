from django.conf.urls import url 
from foodOrdering import views 
 
urlpatterns = [ 
    url(r'^api/orders$', views.orders_list),
    url(r'^api/orders/(?P<pk>[0-9]+)$', views.orders_detail),
    url(r'^api/orders/published$', views.orders_list_published)
]