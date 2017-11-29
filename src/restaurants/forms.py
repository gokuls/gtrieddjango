from django import forms

from .models import RestaurantLocation

from .validators import validate_category

class ResturantLocationCreateForm(forms.ModelForm):
	category 	= forms.CharField(validators=[validate_category])
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
