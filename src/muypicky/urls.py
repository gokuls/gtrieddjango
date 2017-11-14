"""muypicky URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from restaurants.views import ( 
	HomeView,
	AboutView, 
	ContactView, 
	RestaurantView,
	RestaurantDetailView,
	RestaurantCreateView
	)

from restaurants.views import restaurant_listview ,restaurant_createview


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',HomeView.as_view()),
    url(r'^restaurants/$',restaurant_listview),
    #url(r'^restaurantsc/$',restaurant_createview,name="addresto"),
    url(r'^restaurantsc/$',RestaurantCreateView.as_view(),name="addresto"),
    url(r'^restaurants/(?P<slug>\w+)$',RestaurantView.as_view(),name='rlv'),
    url(r'^restaurantsdetail/(?P<slug>[\w-]+)/$',RestaurantDetailView.as_view(),name='rdlv'),
    url(r'^about/$',AboutView.as_view()),
    url(r'^contact/$',ContactView.as_view()),
]
