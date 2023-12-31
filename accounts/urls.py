from django.urls import path
from . import views

from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path("login/", TokenObtainPairView.as_view()),
    path("users/", views.ListCreateUserView.as_view()),
    path("users/<str:user_uuid>/", views.RetrieveUpdateDestroyUserView.as_view()),
]
