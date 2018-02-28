# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django_tables2 import RequestConfig
from django.http import HttpResponse
from prime.models import Doctor, Test
from .tables import DoctorTable, TestTable
from .forms import NameForm, NewForm, LoginForm
from predictor import predictCancer
import numpy as np

import markdown
# Create your views here.


def people(request):
    table = DoctorTable(Doctor.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'prime/table.html', {'table': table})


def tests(request):
    table = TestTable(Test.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'prime/table.html', {'table': table})


def get_name(request):
    # if this is a POST request, we need to process the form data.
    if request.method == 'POST':
        # create a form instance and populate it with data from the request.
        form = NameForm(request.POST)
        # check whether it is valid.
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # print form.cleaned_data
            features = [
                form.cleaned_data['radius_mean'], form.cleaned_data['texture_mean'], form.cleaned_data['perimeter_mean'],
                form.cleaned_data['area_mean'], form.cleaned_data['smoothness_mean'], form.cleaned_data['compactness_mean'],
                form.cleaned_data['concavity_mean'], form.cleaned_data['concave_points_mean'], form.cleaned_data['symmetry_mean'],
                form.cleaned_data['fractal_dimension_mean'], form.cleaned_data['radius_se'], form.cleaned_data['texture_se'],
                form.cleaned_data['perimeter_se'], form.cleaned_data['area_se'], form.cleaned_data['smoothness_se'],
                form.cleaned_data['compactness_se'], form.cleaned_data['concavity_se'], form.cleaned_data['concave_points_se'],
                form.cleaned_data['symmetry_se'], form.cleaned_data['fractal_dimension_se'], form.cleaned_data['radius_worst'],
                form.cleaned_data['texture_worst'], form.cleaned_data['perimeter_worst'], form.cleaned_data['area_worst'],
                form.cleaned_data['smoothness_worst'], form.cleaned_data['compactness_worst'], form.cleaned_data['concavity_worst'],
                form.cleaned_data['concave_points_worst'], form.cleaned_data['symmetry_worst'],
                form.cleaned_data['fractal_dimension_worst']
            ]

            prob, result = predictCancer(np.array(features).reshape(1, -1))
            prob = "Probability : " + str(prob * 100) + "%"
            # print "hello"
            # redirect to a new URL.
            htmlbody = """
                                <html>
                                <body style="background-color:#440977;color:white;font-family: "Times New Roman", Times, serif;">
                                <pre style='text-align:center;font-family: "Times New Roman", Times, serif;color:white;vertical-align:middle'><h1>%s</h1></pre>
                                <pre style='text-align:center;font-family: "Times New Roman", Times, serif;color:white;vertical-align:middle;font-style: italic'><h3>%s</h1></pre>
                                </body>
                                </html>
                                """
            return HttpResponse(htmlbody % (result, prob))
    # if a GET (or any other method) we'l create a blank form.
    else:

        form = NameForm()

    return render(request, 'prime/name.html', {'form': form})


def SSNWebsite(request):
    return render(request, 'prime/SSNwebsite.html')


def blog(request):
    return render(request, 'prime/blog.html')


def login(request):
    return render(request, 'prime/login.html')


def signup(request):
    # if this is a POST request, we need to process the form data.
    if request.method == 'POST':
        # create a form instance and populate it with data from the request.
        form = NewForm(request.POST)
        # check whether it is valid.
        if form.is_valid():
            p = Doctor(doc_id=did, first_name=fname,
                       last_name=lname, salary=sal)
            p.save()

            # process the data in form.cleaned_data as required
            return HttpResponse('<html><body style="background-color:lightblue;"><pre style="text-align:center; letter-spacing:1em; font-size:35px;">Succesfully Signed Up !!</pre></body></html>')

    # if a GET (or any other method) we'l create a blank form.
    else:

        form = NewForm()

    return render(request, 'prime/signup.html', {'form': form})


def about(request):
    return render(request, 'prime/about.html')


def newlogin(request):
    # if this is a POST request, we need to process the form data.
    if request.method == 'POST':
        # create a form instance and populate it with data from the request.
        form = LoginForm(request.POST)
        # check whether it is valid.
        if form.is_valid():
            print form.cleaned_data['d_id']
            print "test"
            # process the data in form.cleaned_data as required
            return HttpResponseRedirect('/users/login/')
    # if a GET (or any other method) we'l create a blank form.
    else:

        form = LoginForm()

    return render(request, 'prime/newlogin.html', {'form': form})
