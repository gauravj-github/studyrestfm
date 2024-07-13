from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        models = User
        fields = ["username","password"]

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # fields = ['name','age']
        # exclude = ['id',]
        fields = '__all__'
    def validate(self , data):
        if data['age']<18:
            raise serializers.ValidationError({"error":"age can not be less then 18"})             
        if data['name']:
            for n in data['name']:
                if n.isdigit():
                    raise serializers.ValidationError({"error":"bsdk naam me number mat dal lodu"})
       
        return data


class Categoryserializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class bookserializer(serializers.ModelSerializer):
    category_name =  Categoryserializer()
    class Meta:
        model = Book
        fields = '__all__'