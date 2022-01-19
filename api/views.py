from rest_framework.views import APIView
from .models import *
from .serializer import *
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

class MovementView(APIView):
	def get(self, request, id):
		movement = get_object_or_404(Movement, id=id)

		return Response(MovementSerializer(movement).data, status=status.HTTP_200_OK)

	def post(self, request):
		serialized = MovementSerializer(data=request.data)
		
		if serializer.is_valid():
			amount = serialized.data.get("amount")
			description = serialized.data.get("description")
			movement = Movement.objects.create(amount=amount, description=description, author=self.request.user.profile)

			return Response(MovementSerializer(movement).data, status=status.HTTP_200_OK)

		return Response({"Bad Request": "Invalid data..."}, status=status.HTTP_400_BAD_REQUEST) 

class GroupView(APIView):
	def get(self, request, id):
		group = get_object_or_404(Group, id=id)

		return Response(GroupSimpleSerializer(group).data, status=status.HTTP_200_OK)

class ProfileView(APIView):
	def get(self, request, id):
		profile = get_object_or_404(Profile, id=id)

		return Response(ProfileSerializer(profile).data, status=status.HTTP_200_OK)
