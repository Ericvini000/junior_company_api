from django.db import models
import uuid


class UserInfo(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    address = models.CharField(max_length=120)
    country = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    biography = models.TextField()
    cpf = models.CharField(max_length=11)
    user = models.OneToOneField("accounts.Account", on_delete=models.CASCADE)
