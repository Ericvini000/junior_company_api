from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class ExperienceLevel(models.TextChoices):
    JUNIOR = "junior"
    JUNIOR1 = "JUNIOR"
    JUNIOR2 = "Junior junior"


class WorkStatus(models.TextChoices):
    EMPLOYED = "employed"
    UNEMPLOYED = "unemployed"


class Account(AbstractUser):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    profile_url = models.URLField(max_length=200)
    experience = models.CharField(
        max_length=14, choices=ExperienceLevel.choices, default=ExperienceLevel.JUNIOR
    )
    status = models.CharField(
        max_length=14, choices=WorkStatus.choices, default=WorkStatus.UNEMPLOYED
    )
