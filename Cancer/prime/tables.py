import django_tables2 as tables
from .models import Doctor,Test

class DoctorTable(tables.Table):
	class Meta:
		model = Doctor
		attrs = {'class' : 'paleblue'}

class TestTable(tables.Table):
	class Meta:
		model = Test
		attrs = {'class' : 'paleblue'}
