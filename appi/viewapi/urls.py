from django.urls import path, include

from viewapi import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employee', views.EmployeeDetails)


# urlpatterns = [
#     path('employee', views.Employeelist.as_view()),
#     path('employee/<int:pk>', views.EmployeeDetails.as_view()),
# ]
urlpatterns = [
    path('', include(router.urls))
]
