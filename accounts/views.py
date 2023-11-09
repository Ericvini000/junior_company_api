from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Account
from .serializers import AccountSerializer


class ListCreateUserView(ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class RetrieveUpdateDestroyUserView(RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    lookup_url_kwarg = "user_uuid"
