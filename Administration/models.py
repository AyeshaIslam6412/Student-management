from django.db import models
from django.conf import settings
# Create your models here.
from student.models import Student


class AdministrationProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='_profile'
    )
    
    first_name = models.CharField(max_length=200,blank=True,null=True)
    last_name = models.CharField(max_length=200,blank=True,null=True)
    Phone_number = models.CharField(max_length=20,blank=True,null=True)
    profile_picture = models.ImageField(upload_to="profile",blank=True,null=True)
    joined_date = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    
    
    def __str__(self):
        return self.user.email if self.user else "No user"
    
class Course(models.Model):
    course_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.course_name
        
         
class Subject(models.Model):
        
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name="subject")
    subject_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.subject_name 
        
        
        
        
class Enrolment(models.Model):
        
    student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name="enrolment")    
    subject = models.ForeignKey(Subject,on_delete=models.ca)  
    
    
    
    
    
   
    
    
   