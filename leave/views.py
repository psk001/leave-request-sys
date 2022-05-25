from urllib import request
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from leave import serializers

# local imports
from leave.serializers import LeaveSerializer, ApplyLeaveSerializer, ApproveLeaveSerializer
from .models import Leave

# lists all the leave requests 
# only admin can see
class EmployeeLeaveList(ListAPIView):
    permission_classes = [IsAdminUser]
    
    def get_queryset(self):
        return Leave.objects.all()

    def get_serializer_class(self):
        return LeaveSerializer

    # def get(self, request):
    #     if request.user.is_superuser:
    #         leave_queryset = Leave.objects.all()
    #         leave_serializer = LeaveSerializer(leave_queryset, many=True)

    #         return Response(leave_serializer.data)
    #     else:
    #         return Response(status=status.HTTP_401_UNAUTHORIZED)


# api to view all leave request of an employee
# requires login
class CurrentUserLeaveList(APIView):

    def get(self, request):
        if request.user.is_superuser:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        user_id = request.user.id
        if user_id is None or request.user.is_superuser:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
        leave_queryset = Leave.objects.filter(user__id=user_id)
        leave_serializer = LeaveSerializer(leave_queryset, many=True)

        return Response(leave_serializer.data)


# api to ask for leave
class ApplyLeave(APIView):
    def post(self, request):
        try:
            user = User.objects.filter(username=request.data['user']).values('pk')[0]['pk']

            data = {'user': user, 'start_date': request.data['start_date'], 'end_date': request.data['end_date']}
    

            serializer = ApplyLeaveSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)

        except AssertionError:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


#api to decide leave request by admin
class GetApproval(APIView):

    def get(self, request, pk):    
        if not request.user.is_superuser:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        leave_queryset = Leave.objects.get(pk=pk)
        leave_serializer = LeaveSerializer(leave_queryset)

        return Response(leave_serializer.data)

    def patch(self, request, pk):
        if not request.user.is_superuser:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        leave_list = Leave.objects.get(pk=pk)
        serializer = ApproveLeaveSerializer(leave_list, data=request.data, partial=True) # set partial=True to update a data partially

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_202_ACCEPTED, data=serializer.data)
        
        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

  





