# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Doctor(models.Model):
    def __unicode__(self):
       return self.doc_id
    doc_id = models.CharField(max_length=50,primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    salary = models.IntegerField(default=250000)


class Test(models.Model):
        def __unicode__(self):
           return self.test_id
        test_id = models.CharField(primary_key=True,max_length=100)
      	log = models.DateTimeField(auto_now=True)
        doc = models.ForeignKey(Doctor,on_delete = models.CASCADE)
        Attributes = models.CharField(max_length=500,default='Haemoglobin, WBC')
        numattr = models.IntegerField(default=10)
        Classification_Status = models.CharField(max_length=5,default="Yes")
