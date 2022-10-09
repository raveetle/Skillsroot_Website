from django.db import models
from django.contrib.auth.models import User
from adminapp.models import Course

# Create your models here.

class Client(models.Model):
  name =  models.CharField(max_length = 200,null = True)
  phone= models.CharField(max_length=200,null = True)
  email= models.EmailField(null = True)
  date_created=models.DateTimeField(auto_now_add=True,null = True)
  dob=models.DateField(null = True)
  gender=models.CharField(max_length=200,null = True,choices=[('Male','Male'),('Female','Female'),('Others','Others')])
  adhar_card = models.FileField(upload_to='documents')
  user = models.OneToOneField(User,on_delete=models.CASCADE)

  def __str__(self):
    return self.name

class  Skill(models.Model):
  name = models.CharField(max_length = 200,null = True)
   
  def __str__(self):
    return self.name

class Loan(models.Model):
  client = models.ForeignKey(Client,on_delete= models.DO_NOTHING)
  amount =  models.FloatField()
  description=  models.CharField(max_length=200)
  collatral = models.FileField(upload_to='documents')
  adharCard= models.FileField(upload_to='documents')
  panCard = models.FileField(upload_to='documents')
  category = models.CharField(max_length=200, null=True)
  status = models.CharField(max_length = 200,choices=[('Pending','Pending'),('Approved','Approved'),('Rejected','Rejected')], default=('Pending, Pending'))

class CourseEnrollment(models.Model):
  course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
  client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
  enrolled_on = models.DateTimeField(auto_now_add=True)
  status = models.CharField(max_length=200, choices=[('In Progress', 'In Progress'), ('Completed', 'Completed')])

  def __str__(self):
    return self.client + '-' + self.course



  
