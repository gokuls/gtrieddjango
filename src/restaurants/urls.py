from django.conf.urls import url
from django.contrib import admin

from django.contrib.auth.views import LoginView

from django.contrib.auth.views import LogoutView

from restaurants.views import ( 
	RestaurantView,
	RestaurantDetailView,
	RestaurantCreateView
	)

from restaurants.views import restaurant_listview ,restaurant_createview


urlpatterns = [
    url(r'^$',restaurant_listview),
    url(r'^restaurantsc/$',RestaurantCreateView.as_view(),name="addresto"),
    url(r'^(?P<slug>\w+)$',RestaurantView.as_view(),name='rlv'),
    url(r'^(?P<slug>[\w-]+)/$',RestaurantDetailView.as_view(),name='rdlv'),
]
