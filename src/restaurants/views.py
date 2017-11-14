from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import random
from django.views import View


from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic import CreateView

#import models

from .models import RestaurantLocation

#import forms 

from .forms import ResturantLocationCreateForm


# Create your views here.


#Function based view

# def home(request):
# 	num = random.randint(0,1000000)
# 	somelist = [num,random.randint(0,1000000),random.randint(0,1000000)]
# 	context = {
# 		"html_var":"context variable",
# 		"bool_item":True,
# 		"num":num,
# 		"some_list":somelist
# 		}
# 	return  render(request,"home.html",context)

# def about(request):
# 	num = random.randint(0,1000000)
# 	somelist = [num,random.randint(0,1000000),random.randint(0,1000000)]
# 	context = {
		
# 		}
# 	return  render(request,"about.html",context)

# def contact(request):
# 	num = random.randint(0,1000000)
# 	somelist = [num,random.randint(0,1000000),random.randint(0,1000000)]
# 	context = {
		
# 		}
# 	return  render(request,"contact.html",context)

class HomeView(TemplateView):
	template_name = "home.html"

	def get_context_data(self, *args,**kwargs):
		context = super(HomeView,self).get_context_data(*args,**kwargs)
		num = random.randint(0,1000000)
		somelist = [num,random.randint(0,1000000),random.randint(0,1000000)]
		context = {
			"html_var":"context variable",
			"bool_item":True,
			"num":num,
			"some_list":somelist
			}
		return context


class AboutView(TemplateView):
	template_name = "about.html"


class ContactView(TemplateView):
	template_name = "contact.html"

def restaurant_listview(request):
	template_name = "restaurants/restaurants_list.html"
	objl = RestaurantLocation.objects.all()
	context = {
		"object_list": objl
	}
	return render(request,template_name,context)

class RestaurantView(ListView):
	#queryset = RestaurantLocation.objects.filter(location='Chennai')
	template_name = "restaurants/restaurants_list.html"

	def get_queryset(self):
		slug = self.kwargs.get("slug")
		print(slug)
		if slug:
			queryset = RestaurantLocation.objects.filter(location__iexact=slug)
		else:
			queryset = RestaurantLocation.objects.none()
		return queryset

class RestaurantDetailView(DetailView):
	queryset = RestaurantLocation.objects.all()

	# def get_context_data(self, *args, **kwargs):
	# 	print(self.kwargs)
	# 	context = super(RestaurantDetailView, self).get_context_data(*args, **kwargs)
	# 	print(context)
	# 	return context	

	# def get_object(self, *args, **kwargs):
	# 	rest_id = self.kwargs.get('rest_id')
	# 	obj = get_object_or_404(RestaurantLocation,id=rest_id) # pk = rest_id
	# 	return obj

def restaurant_createview(request):
	form = ResturantLocationCreateForm(request.POST or None)
	errors = None

	if form.is_valid():
		form.save()
		return HttpResponseRedirect("/restaurants/")

	if form.errors:
		errors = form.errors

	template_name = 'restaurants/forms.html'
	context = {'form':form,"errors":errors}

	return render(request,template_name,context)

class RestaurantCreateView(CreateView):
	form_class 		= ResturantLocationCreateForm
	template_name 	= 'restaurants/forms.html'	
	success_url 	= '/restaurants/'
