# serializers.py 

from rest_framework import serializers
from .models import ML_Model 


class ML_Model_Serializer(serializers.HyperlinkedModelSerializer):
    ## I have no idea what the fuck a serializer even is but we'll learn 
    class Meta: ## holds the metadata (data of the data)
        model = ML_Model 
        fields = ('alias', 'accuracy', 'log_console_print') 
        