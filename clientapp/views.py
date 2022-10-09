from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from clientapp.models import Client, Loan
from django.contrib.auth.models import User
from adminapp.models import Course, Trainer
from recapp.models import Job

def landing(request):
    return render(request, 'clientapp/index.html')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('coursesPage')
        else:
            return render(request, 'clientapp/login.html', {'msg': 'Invalid credentials'})
    return render(request, 'clientapp/login.html')

def signupPage(request): 
    data={}
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        conf_pass = request.POST.get('password_cnfrm')
        if username  == '':
            data['error'] = 'Empty field (fullname) not permitted'
        if email == '':
            data['error'] = 'Empty field (email) not permitted'
        
        if 'error' in  data.keys():
            return render(request, 'clientapp/signup.html', data)
        if password != '' and conf_pass != '' and password == conf_pass:
            fullnamearr = username.split(' ')
            firstname, lastname = fullnamearr[0], ''.join(fullnamearr[1:])
            user= User.objects.create_user(username = username.replace(' ',''), email=email,password= password)
            user.first_name = firstname
            user.last_name = lastname
            user.save()
            ct = Client.objects.create(
                name = username,
                email = email,
                user = user
                )
            ct.save()
            return redirect('loginPage')
        

    return render(request, 'clientapp/signup.html',data)

def dashboardPage(request):
    return render(request, 'clientapp/dashboard.html', {'user': request.user})

def coursesPage(request):
    courses = Course.objects.all() 
    return render(request, 'clientapp/courses.html', {'user': request.user, 'courses': courses})

def profile(request):
    context = {'client': Client.objects.get(user = request.user), 'user': request.user}
    return render(request, 'clientapp/profile.html', context)


def applyLoan(request):
    status=False
    if request.method == 'POST':
        aadhar = request.FILES.get('aadhar')
        pan = request.FILES.get('pan')
        bank_statement = request.FILES.get('bank_statement')
        photograph = request.FILES.get('photograph')
        amount = request.POST.get('amount')
        category = request.POST.get('inlineRadioOptions2')
        gender = request.POST.get('gender')
        description = request.POST.get('description')
        if aadhar is not None and pan is not None and bank_statement is not None and photograph is not None:
            cl = Client.objects.get(user=request.user)
            loan = Loan.create(
                client = cl,
                category = category, 
                amount = amount,
                gender = gender,
                adharCard = aadhar,
                panCard = pan,
                collatral = bank_statement,
                description = description
            )
            loan.save()
            return redirect('dashboard')
        cl = Client.objects.get(user=request.user)
        allLoans = Loan.objects.all()
        status = False
        for i in allLoans:
            if(i.client == cl):
                status = True
                break
    return render(request, 'clientapp/applyLoans.html' , {'user': request.user, 'status': status | False})

def applyTrainer(request):
    courses = Course.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        aadhar = request.FILES.get('aadhar')
        sector = request.POST.get('sector')
        course = request.POST.get('course')
        cv = request.FILES.get('cv')
        tot = request.FILES.get('tot')
        marksheet = request.FILES.get('marksheet')
        if name is not None and phone is not None and aadhar is not None and sector is not None and course is not None and cv is not None and tot is not None and marksheet is not None:
            cl = Client.objects.get(user=request.user)
            tr = Trainer.create(
                name=name,
                phone=str(phone),
                aadharCard=aadhar,
                cV=cv,
                sector=sector,
                course = Course.objects.get(name=course),
                marksheet=marksheet,
                tot_Certificate=tot
            )
            tr.save()
            return redirect('dashboard')
    return render(request, 'clientapp/apply_trainer.html' , {'user': request.user, 'courses': courses})

def logoutApp(request):
    logout(request)
    return redirect('loginPage')

def chartPage(request):
    return render(request, 'clientapp/profile.html')

def viewJobs(request):
    jobs = Job.objects.all()
    return render(request, 'clientapp/viewJobs.html', {'jobs': jobs, 'user': request.user})


   
