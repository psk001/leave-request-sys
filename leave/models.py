from importlib.metadata import requires
from operator import truediv
from django.db import models
from django.contrib.auth.models import User, AbstractUser


# class User(AbstractUser, models.Model):
#     username = models.CharField(max_length=255, unique=True, primary_key=True)


class Leave(models.Model):
    LEAVE_STATUS_CHOICE = [
        ('PD', 'pending'),
        ('AP', 'approved'),
        ('DA', 'disapproved')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    status = models.CharField(max_length=2, choices=LEAVE_STATUS_CHOICE, default='PD')
    requested_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField()
    end_date = models.DateField()

