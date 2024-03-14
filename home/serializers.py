from rest_framework import serializers
from .models import Person
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

        def validate(self, data):
            if data['username']:
                if User.objects.filter(username=data['username']).exists():
                   raise serializers.ValidationError('username Taken')

            if data['email']:
                if User.objects.filter(email=data['email']).exists():
                   raise serializers.ValidationError('Email Taken')
            return data

        def create(self, validated_data):
            user=User.objects.create(username=validated_data['username'], email=validated_data['email'])
            user.set_password(validated_data['password'])
            user.save()
            return validated_data








# class RegisterSerializer(serializers.Serializer):
#     username=serializers.CharField()
#     email=serializers.EmailField()
#     password=serializers.CharField()
#     def validate(self, data):
#         if data['username']:
#             if User.objects.filter(username=data['username']).exists():
#                raise serializers.ValidationError('username Taken')

#         if data['email']:
#             if User.objects.filter(email=data['email']).exists():
#                raise serializers.ValidationError('Email Taken')
#         return data
#     def create(self, validated_data):
#         user=User.objects.create(username=validated_data['username'],email=validated_data['email'])
#         user.set_password(validated_data['password'])
#         user.save()
#         return validated_data

 



# class LoginSerializer(serializers.Serializer):
#     username=serializers.CharField()
#     password=serializers.CharField()
#     def validate(self, data):
#         if data['username']:
#             if User.objects.filter(username=data['username']).exists():
#                raise serializers.ValidationError('username Taken')
#     def create(self, validated_data):
#         user=User.objects.create(username=validated_data['username'])
#         user.set_password(validated_data['password'])
#         user.save()
#         return validated_data




class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Person
        fields = '__all__'


    def validate(self, data):
        if 'age' in data:
            try:
                age = int(data['age'])
                if age < 18:
                    raise serializers.ValidationError("Age must be greater than or equal to 18")
            except (KeyError, ValueError):
                raise serializers.ValidationError("Invalid age value")
        return data
