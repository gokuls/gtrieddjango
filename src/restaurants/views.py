from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import random
from django.views import View


from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic import UpdateView
from django.views.generic import CreateView

#import models

from .models import RestaurantLocation

#import forms 

from .forms import ResturantLocationCreateForm

# Create your views here.


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

class RestaurantView(LoginRequiredMixin, ListView):
	#queryset = RestaurantLocation.objects.filter(location='Chennai')
	template_name = "restaurants/restaurants_list.html"

	def get_queryset(self):
		return RestaurantLocation.objects.filter(owner = self.request.user )


class RestaurantDetailView(LoginRequiredMixin, DetailView):
	def get_queryset(self):
		return RestaurantLocation.objects.filter(owner = self.request.user )
		#queryset = RestaurantLocation.objects.filter(owner = self.request.user) # filter(owner = self.request.user )



class RestaurantCreateView(LoginRequiredMixin, CreateView):
	login_url='/login/'
	form_class 		= ResturantLocationCreateForm
	template_name 	= 'forms.html'	
	#success_url 	= '/restaurants/'

	def form_valid(self,form):
		instance = form.save(commit=False)

		instance.owner = self.request.user

		return super(RestaurantCreateView,self).form_valid(form )

	def get_context_data(self, *args, **kwargs):
		context 	= 	super(RestaurantCreateView, self).get_context_data(*args, **kwargs)
		context['title'] 	= 	"Add Restaurants"
		return context

class RestaurantUpdateView(LoginRequiredMixin, UpdateView):
	login_url='/login/'
	form_class 		= ResturantLocationCreateForm
	template_name 	= 'restaurants/detail-update.html'	
	#success_url 	= '/restaurants/'

	def get_queryset(self):
		return RestaurantLocation.objects.filter(owner = self.request.user )

	def get_context_data(self, *args, **kwargs):
		context 	= 	super(RestaurantUpdateView, self).get_context_data(*args, **kwargs)
		context['title'] 	= 	"Add Restaurants"
		return context





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



# def restaurant_listview(request):
# 	template_name = "restaurants/restaurants_list.html"
# 	objl = RestaurantLocation.objects.all()
# 	context = {
# 		"object_list": objl
# 	}
# 	return render(request,template_name,context)


	# def get_context_data(self, *args, **kwargs):
	# 	print(self.kwargs)
	# 	context = super(RestaurantDetailView, self).get_context_data(*args, **kwargs)
	# 	print(context)
	# 	return context	

	# def get_object(self, *args, **kwargs):
	# 	rest_id = self.kwargs.get('rest_id')
	# 	obj = get_object_or_404(RestaurantLocation,id=rest_id) # pk = rest_id
	# 	return obj

# def restaurant_createview(request):
# 	form = ResturantLocationCreateForm(request.POST or None)
# 	errors = None

# 	if form.is_valid():
# 		if request.user.is_authenticated():
# 			instance = form.save(commit=False)
# 			instance.owner = request.user
# 			instance.save()
# 			return HttpResponseRedirect("/restaurants/")

# 	if form.errors:
# 		errors = form.errors

# 	template_name = 'restaurants/forms.html'
# 	context = {'form':form,"errors":errors}

# 	return render(request,template_name,context)


