from django.conf.urls import url

from . import views

urlpatterns = [
 url(r'^newlogin/',views.newlogin,name='newlogin'),
 url(r'^about/',views.about,name='about'),
 url(r'^signup/',views.signup,name='signup'),
 url(r'^login/',views.login,name='login'),
 url(r'^input/',views.get_name,name='get_name'),
 url(r'^doctors/',views.people,name='people'),
 url(r'^tests/',views.tests,name='tests'),
 url(r'^',views.blog,name='blog'),
]
