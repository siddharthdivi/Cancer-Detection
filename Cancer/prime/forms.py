from django import forms
from django.utils.safestring import mark_safe
from prime.models import Doctor,Test
from django.forms.models import inlineformset_factory

class NewForm(forms.Form):
    #your_name : First Name
    your_name = forms.CharField(label=' First Name ',max_length=100,initial='Hello')
    last_name = forms.CharField(label='  Last Name  ',max_length=100)
    doc_id = forms.CharField(label=' Registered ID  ',max_length=100)
    salary = forms.IntegerField(label=' Salary         ')


class LoginForm(forms.Form):
    #your_name : First Name
    d_id = forms.CharField(label='Doc_ID',max_length=100,initial='IND123')

class NameForm(forms.Form):
    radius_mean = forms.FloatField(label=' Radius_Mean ',initial = 14.12729)
    texture_mean = forms.FloatField(label=' Texture_Mean ',initial = 19.28964)
    perimeter_mean = forms.FloatField(label=' Perimeter_Mean ',initial = 91.96903)
    area_mean = forms.FloatField(label=' Area_Mean ',initial = 654.88910)
    smoothness_mean = forms.FloatField(label=' Smoothness_Mean ',initial = 0.09636)
    compactness_mean = forms.FloatField(label=' Compactness_Mean ',initial = 0.10434)
    concavity_mean = forms.FloatField(label=' Concavity_Mean ',initial = 0.08879)
    concave_points_mean = forms.FloatField(label=' Concave Points_Mean ',initial = 0.04891)
    symmetry_mean = forms.FloatField(label=' Symmetry_Mean ',initial = 0.18116)
    fractal_dimension_mean = forms.FloatField(label=' Fractal_Dimension_Mean ',initial = 0.06279)

    radius_se = forms.FloatField(label=' Radius_se',initial = 0.40517)
    texture_se = forms.FloatField(label=' texture_se',initial = 1.21685)
    perimeter_se = forms.FloatField(label=' Perimeter_se',initial = 2.86605)
    area_se = forms.FloatField(label=' Area_se ',initial = 40.33707)
    smoothness_se = forms.FloatField(label=' Smoothness_se ',initial = 0.00704)
    compactness_se = forms.FloatField(label=' Compactness_se ',initial = 0.02547)
    concavity_se = forms.FloatField(label=' Concavity_se ',initial = 0.031893)
    concave_points_se = forms.FloatField(label=' Concave Points_se ',initial = 0.011796)
    symmetry_se = forms.FloatField(label=' Symmetry_se ',initial = 0.020542)
    fractal_dimension_se = forms.FloatField(label=' Fractal_Dimension_se ',initial = 0.00379)

    radius_worst = forms.FloatField(label=' Radius_worst ',initial = 16.26918)
    texture_worst = forms.FloatField(label=' Texture_worst ',initial = 25.67722)
    perimeter_worst = forms.FloatField(label=' Perimeter_worst ',initial = 107.26121)
    area_worst = forms.FloatField(label=' Area_worst ',initial = 880.58312)
    smoothness_worst = forms.FloatField(label=' Smoothnes_worst ',initial = 0.13236)
    compactness_worst = forms.FloatField(label=' Compactness_worst ',initial = 0.25426)
    concavity_worst = forms.FloatField(label=' Concavity_worst ',initial = 0.272188)
    concave_points_worst = forms.FloatField(label=' Concave Points_worst ',initial = 0.11460)
    symmetry_worst = forms.FloatField(label=' Symmetry_worst',initial = 0.29007)
    fractal_dimension_worst = forms.FloatField(label=' Fractal_Dimension_worst ',initial = 0.08394)
