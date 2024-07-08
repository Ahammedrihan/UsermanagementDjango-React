from rest_framework import serializers
from .models import Accounts



class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only = True)
    class Meta:
        model = Accounts
        fields = ['email','name','phone','password','password2']


    def validate(self, attrs):
        password1 = attrs.get('password')
        password2 = attrs.get('password2')
        if password1 != password2:
            raise serializers.ValidationError("password does not match")
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password2')
        return Accounts.objects.create_user(**validated_data)
    



class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        exclude = ['password']


