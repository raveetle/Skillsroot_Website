from django.urls import path
from . import views

urlpatterns = [

    path('add_job/', views.addJob, name='add_job'),
    path('', views.landing, name='landing'),
    path('login/', views.loginPage, name='recloginPage'),
    path('signup/', views.signupPage, name='recsignupPage'),
    path('view-applicants/', views.track_applicationsPage, name='viewApplicants'),
    path('logout/', views.logoutApp)
]