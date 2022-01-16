from .models import *
from django.db.models import fields
from rest_framework import serializers

class MovementSerializer(serializers.ModelSerializer):
	class Meta:
		model = Movement
		fields = ("__all__")