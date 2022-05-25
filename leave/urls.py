from django.urls import URLPattern, path
from django.contrib.auth.decorators import login_required
from . import views

# router = DefaultRouter()

urlpatterns = [
    path('leaves', views.EmployeeLeaveList.as_view()),
    path('me', login_required(views.CurrentUserLeaveList.as_view())),
    path('applyleave', views.ApplyLeave.as_view()),
    path('getapproval/<int:pk>', views.GetApproval.as_view())
]


