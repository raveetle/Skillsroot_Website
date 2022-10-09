from django.shortcuts import render,redirect
from recapp.models import Job
from clientapp.models import Skill
from django.contrib.auth import authenticate, login , logout
from recapp.models import Application, Company
from clientapp.models import Client
from django.contrib.auth.models import User

def addJob(request):
    companies = Company.objects.all()
    if request.method == 'POST':
        company = request.POST.get('company')
        location = request.POST.get('location')
        salary = request.POST.get('salary')
        job_title = request.POST.get('job_title')
        deadline = request.POST.get('deadline')
        skills = request.POST.get('skills').split(',')
        sks = []
        for s in skills:
            print(s)
            sks.append(Skill.objects.get(name=s))
        if company is not None and location is not None and salary is not None and job_title is not None:
            jb = Job.create(
                job_title=job_title,
                salary=salary,
                company=Company.objects.get(name=company),
                deadline=deadline,
                skills=sks
            )
            jb.save()
            return redirect('viewApplicants')

    return render(request, 'recapp/add_job.html' , {'user': request.user, 'companies': companies})

def landing(request):
    return render(request, 'recapp/index.html')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('viewApplicants')
        else:
            return render(request, 'recapp/login.html', {'msg': 'Invalid credentials'})
    return render(request, 'recapp/login.html')

def logoutApp(request):
    logout(request)
    return redirect('recloginPage')


def signupPage(request):
    data={} 
    if request.method == 'POST':
        
        fullname = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if fullname == '':
            data['error'] = 'Empty field (fullname) not permitted'
        if email == '':
            data['error'] = 'Empty field (email) not permitted'
        if 'error' in  data.keys():
            return render(request, 'recapp/signup.html', data)
        if password != '':
            fullnamearr = fullname.split(' ')
            firstname, lastname = fullnamearr[0], ''.join(fullnamearr[1:])
            user= User.objects.create_user(username = fullname.replace(' ',''),password= password)
            user.first_name = firstname
            user.last_name = lastname
            user.save()
            ct = Company.objects.create(
                name = fullname,
                email = email,
                user = user
                )
            ct.save()
            return redirect('recloginPage')
    return render(request, 'recapp/signup.html',data)

def track_applicationsPage(request):
    cmp = Company.objects.get(user = request.user)
    applications = Application.objects.filter(company = cmp)
    if request.method == 'POST':
        decision = request.POST.get('decision')
        email = request.POST.get('email')
        cl = Client.objects.get(email=email)
        ap = Application.objects.get(applicant=cl)
        ap.status = decision
        ap.save()
        return redirect('viewApplicants')
    return render(request, 'recapp/track_applicants.html', {'applications': applications, 'user': request.user})