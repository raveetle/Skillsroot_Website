from django.urls import path
from adminapp.views import *

urlpatterns = [
    path('viewCourses/', viewCourses, name='viewCourses'),
    path('viewJobs', viewJobs, name='viewJobs'),
    path('updateLoan', updateLoan, name='updateLoan'),

]