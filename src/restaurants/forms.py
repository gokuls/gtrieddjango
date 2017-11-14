from django import forms

from .models import RestaurantLocation

class ResturantLocationCreateForm(forms.ModelForm):
	class Meta:
		model 	= RestaurantLocation
		fields 	= [
				'name',
				'location',
				'category',
		]

	def clean_name(self):
		name = self.cleaned_data.get("name")
		if name == "hello":
			raise forms.ValidationError("Not a valid input ")
		return name
