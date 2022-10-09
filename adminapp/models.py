from django.db import models

class Course(models.Model):
   name= models.CharField(max_length=200)
   id= models.CharField(max_length=200, primary_key=True)
   level=models.CharField(max_length=50, choices=[('Easy','Easy'),('Medium','Medium'),('Hard','Hard')])
   hours=models.FloatField(max_length=100)
   class_training= models.FloatField(max_length=200)
   lab_training= models.FloatField(max_length=200)
   
   def __str__(self):
      return self.name 

class Trainer(models.Model):
   name= models.CharField(max_length=200,null=True)
   phone=models.CharField(max_length=20,null=True)
   aadharCard=models.FileField(upload_to='documents')
   cV=models.FileField(upload_to='documents')
   sector=models.CharField(max_length=200,null=True,choices=[('Food Processing','Food Processing'),('Beauty & Wellness','Beauty & Wellness'),('Retail','Retail'),('Apparel','Apparel'),('Domestic Workers','Domestic Workers')])
   course=models.ForeignKey(Course, on_delete=models.DO_NOTHING)
   marksheet=models.FileField(upload_to='documents')
   tot_Certificate=models.FileField(upload_to='documents')
   def __str__(self):
      return self.name
