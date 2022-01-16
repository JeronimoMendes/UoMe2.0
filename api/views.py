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

	
