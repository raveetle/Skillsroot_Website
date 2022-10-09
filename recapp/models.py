from django.db import models
from clientapp.models import Client
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.name

class Skill(models.Model):
    name =  models.CharField(max_length=200, null=True)

class Job(models.Model):
    job_title = models.CharField(max_length=200, null=True)
    salary = models.CharField(max_length=200, null=True)
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    deadline = models.DateTimeField(null=True)
    location = models.CharField(max_length=800)
    skills = models.ManyToManyField(Skill)
    def __str__(self):
        return self.job_title + '-' + self.company.name + '-' + self.location


class Application(models.Model):
    applicant = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    job = models.ForeignKey(Job, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=200, null=True, choices = [('Accepted', 'Accepted'), ('Rejected', 'Rejected'), ('Pending', 'Pending')])
    applied_on = models.DateTimeField(auto_created=True, auto_now_add=True)
    
    def __str__(self):
        return self.applicant.name + '-' + self.company.name + '-' + self.job.job_title