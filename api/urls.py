from django.urls import path
from .views import *

urlpatterns = [
    path("movement/<int:id>", MovementView.as_view()),
]