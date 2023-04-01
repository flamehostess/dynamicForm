from rest_framework import serializers
from .models import *

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = [
            'id',
            'name_job',
            'release_dates',
            'due_dates'
        ]