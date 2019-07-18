# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
## we will literally create a model 
## to store all the hyperparameters 
## of our machine learning models (implemented via Naive Bayes) 
## and the results / predictions / accuracy rates of those models

class ML_Model(models.Model):
    alias = models.CharField(max_length=60)
    accuracy = models.CharField(max_length=60) ## stores the final accuracy [0, 1] of the model 
    log_console_print = models.TextField(max_length=2048) ## stores the final printed out from the log console of the model  
    

    def __str__(self): 
        return self.alias 
