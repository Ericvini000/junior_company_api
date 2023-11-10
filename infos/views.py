from rest_framework.generics import ListCreateAPIView
from .serializers import UserInfoSerializer
from .models import UserInfo
from rest_framework_simplejwt.authentication import JWTAuthentication


class ListCreateInfoView(ListCreateAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer

    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        found_user = self.request.user
        return serializer.save(user=found_user)
