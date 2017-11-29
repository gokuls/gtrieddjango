from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView

from .models import Item

from .forms import ItemForm

class ItemListView(LoginRequiredMixin, ListView):
	def get_queryset(self):
		return Item.objects.filter(user=self.request.user)


class ItemDetailView(LoginRequiredMixin, DetailView):
	def get_queryset(self):
		return Item.objects.filter(user=self.request.user)


class ItemCreateView(LoginRequiredMixin, CreateView):
	template_name = 'forms.html'
	form_class 	=	ItemForm
	def get_queryset(self):
		return Item.objects.filter(user=self.request.user)

	def form_valid(self,form):
		obj = form.save(commit=False)
		obj.user = self.request.user
		return super(ItemCreateView, self ).form_valid(form)

	def get_form_kwargs(self):
		kwargs = super(ItemCreateView,self).get_form_kwargs()
		kwargs['user'] = self.request.user
		return kwargs 

	def get_context_data(self, *args, **kwargs):
		context 	= 	super(ItemCreateView, self).get_context_data(*args, **kwargs)
		context['title'] 	= 	"Create Item"
		return context


class ItemUpdateView(LoginRequiredMixin,  UpdateView):
	template_name = 'forms.html'
	form_class 	=	ItemForm
	def get_queryset(self):
		return Item.objects.filter(user=self.request.user)

	def get_context_data(self, *args, **kwargs):
		context 	= 	super(ItemUpdateView, self).get_context_data(*args, **kwargs)
		context['title'] 	= 	"Update Item"
		return context

	def get_form_kwargs(self):
		kwargs = super(ItemUpdateView,self).get_form_kwargs()
		kwargs['user'] = self.request.user
		return kwargs 

