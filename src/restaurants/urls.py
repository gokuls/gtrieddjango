from django.conf.urls import url
from django.contrib import admin

from django.contrib.auth.views import LoginView

from django.contrib.auth.views import LogoutView

from restaurants.views import ( 
	RestaurantView,
	RestaurantDetailView,
	RestaurantCreateView,
	RestaurantUpdateView
	)


urlpatterns = [
    url(r'^$',RestaurantView.as_view(), name="listview"),
    url(r'^restaurantsc/$',RestaurantCreateView.as_view(),name="create"),
    #url(r'^(?P<slug>\w+)$',RestaurantView.as_view(),name='rlv'),
    #url(r'^(?P<slug>[\w-]+)/$',RestaurantDetailView.as_view(),name='rdlv'),
    url(r'^(?P<slug>[\w-]+)/$',RestaurantUpdateView.as_view(),name='edit'),
]
