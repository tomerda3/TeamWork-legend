import django_filters
from django_filters import CharFilter

from .models import *

class HostingPlaceFilter(django_filters.FilterSet):
	name = CharFilter(field_name='name', lookup_expr='icontains')
	location = CharFilter(field_name='location', lookup_expr='icontains')

	class Meta:
		model = HostingPlace
		fields = '__all__'
		exclude = ['username']