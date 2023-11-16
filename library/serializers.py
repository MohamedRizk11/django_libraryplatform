from rest_framework import serializers
from .models import Book,Author



class autherserializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields='__all__'

class bookserializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'
        
        


