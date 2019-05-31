# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

class Event(models.Model):
  id = models.AutoField(primary_key=True)
  Title = models.CharField(max_length=50)
  Description = models.CharField(max_length=1000)
  StartDate = models.DateField()
  EndDate = models.DateField()
  Category = models.CharField(max_length=50)