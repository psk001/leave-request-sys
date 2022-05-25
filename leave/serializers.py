from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Leave


# default serializer for user model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username']


# default serializer for leave 
class LeaveSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model= Leave
        fields = ['user', 'requested_at', 'status', 'start_date', 'end_date']


# serializer to leave details of current logged in user
class CurrentUserLeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leave
        fields = ['start_date', 'end_date', 'requested_at', 'status']     


# serializer to apply for leave
class ApplyLeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leave
        fields = ['user', 'start_date', 'end_date']   


class ApproveLeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leave
        fields = ['status']   


