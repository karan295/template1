from rest_framework import serializers
from .models import student_model

class student_serializer(serializers.ModelSerializer):
    #name=serializers.CharField(read_only=True)
    
    # we cannot post name because it is only for read only
    class Meta:
        model=student_model
        fields=['name','roll','city']

        # field level validations
        def validate_roll(self,value):
            if value>=200:
                raise serializers.ValidationError('seat full')
            return value
        
        #object level validations
        
        def validate(self,data):
            nm=data.get('name')
            ct=data.get('city')
            if nm.lower()=='rohit' and ct.lower()=='ranchi':
                raise serializers.ValidationError('city must be ranchi')
