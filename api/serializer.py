from .models import *
from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User

class MovementSerializer(serializers.ModelSerializer):
	class Meta:
		model = Movement
		fields = ("__all__")

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ("email")

class GroupSimpleSerializer(serializers.ModelSerializer):
	movement = MovementSerializer(many=True)

	class Meta:
		model = Group
		fields = ("name", "movement")
