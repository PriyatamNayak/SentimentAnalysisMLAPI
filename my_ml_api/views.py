# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets 

from .serializers import ML_Model_Serializer
from .models import ML_Model

# Create your views here.

class ML_ModelViewSet(views.ModelViewSet): 
    queryset = ML_Model.objects.all().order_by('alias')
    serializer_class = ML_Model_Serializer
