from django.urls import path
from clientapp.views import *
urlpatterns = [
    path('', landing, name='landing'),
    path('login/', loginPage, name='loginPage'),
    path('signup/', signupPage, name='signupPage'),
    path('dashboard/', dashboardPage, name='dashboardPage'),
    path('profile/', profile, name='profilePage'),
    path('courses/', coursesPage, name='coursesPage'),
    path('logout/', logoutApp, name='logout'),
    path('test/', chartPage),
    path('applyLoans/', applyLoan, name='applyLoans'),
    path('viewJobs/', viewJobs, name='viewJobs'),
]