from django.shortcuts import render
from clientapp.models import Loan,Client
from adminapp.models import Course
from recapp.models import Job,Company

# Create your views here.
def viewCourses(request):
    context = {
        'courses':Course.objects.all()
    }
    #change HTML accordingly
    return render(request, 'adminapp/index.html', context)

def viewJobs(request):
    context = {
        'jobs':Job.objects.all(),
        'company': Company.objects.all()
    }

#update loan status
def updateLoan(request):
    context= {
        'loans':Loan.objects.all()
    }
