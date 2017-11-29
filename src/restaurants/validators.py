from django.core.exceptions import ValidationError

from django.utils.translation import ugettext_lazy as _	

def validate_even(value):
	if value % 2 != 0:
		raise ValidationError(
			_('%(value)s is not a even number'),
			params = {'value':value},
			)

CATEGORIES = ['veg', 'non-veg']

def validate_category(value):
	if not value in CATEGORIES:
		raise ValidationError("%s This is not a Valid category "%value)