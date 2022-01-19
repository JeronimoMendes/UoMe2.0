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
	movements = MovementSerializer(many=True)

	class Meta:
		model = Group
		fields = ("name", "movements")

class ProfileSimpleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = ("id",)

class RelationSerializer(serializers.ModelSerializer):
	movements = MovementSerializer(many=True)
	user1 = ProfileSimpleSerializer()
	user2 = ProfileSimpleSerializer()

	class Meta: 
		model = Relation
		fields = ("__all__")

class ProfileSerializer(serializers.ModelSerializer):
	groups = GroupSimpleSerializer(many=True)
	relations = serializers.SerializerMethodField()

	class Meta:
		model = Profile
		fields = ("groups", "id", "relations")

	def get_relations(self, obj):
		relations = Relation.objects.filter(user1=obj)
		relations |= Relation.objects.filter(user2=obj)

		return RelationSerializer(relations, many=True).data
