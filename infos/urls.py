from django.urls import path
from . import views


urlpatterns = [path("users/<str:user_uuid>/infos", views.ListCreateInfoView.as_view())]
