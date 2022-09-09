from django.db import models
from django.contrib.auth.models import User
# error imports
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CustomUser(AbstractUser):

	is_student=models.BooleanField(default=False)
	is_teacher=models.BooleanField(default=False)
	is_admin=models.BooleanField(default=False)

    objects=CustomUser()


class TeacherExtra(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    salary = models.PositiveIntegerField(null=False)
    joindate=models.DateField(auto_now_add=True)
    mobile = models.CharField(max_length=40)
    status=models.BooleanField(default=False)
    def __str__(self):
        return self.user.first_name
    @property
    def get_id(self):
        return self.user.id
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name




classes=[('one','one'),('two','two'),('three','three'),
('four','four'),('five','five'),('six','six'),('seven','seven'),('eight','eight'),('nine','nine'),('ten','ten')]
class StudentExtra(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    roll = models.CharField(max_length=10)
    mobile = models.CharField(max_length=40,null=True)
    fee=models.PositiveIntegerField(null=True)
    cl= models.CharField(max_length=10,choices=classes,default='one')
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name



class Attendance(models.Model):
    roll=models.CharField(max_length=10,null=True)
    date=models.DateField()
    cl=models.CharField(max_length=10)
    present_status = models.CharField(max_length=10)



class Notice(models.Model):
    date=models.DateField(auto_now=True)
    by=models.CharField(max_length=20,null=True,default='school')
    message=models.CharField(max_length=500)



# Create your models here.

# class CustomUser(AbstractUser):
# 	username = None 
# 	email = models.EmailField(unique=True)
# 	is_admin=models.BooleanField(default=False)
# 	is_employer=models.BooleanField(default=False)
# 	is_employee=models.BooleanField(default=False)
# 	slug = models.SlugField(blank=True, unique=True)
# 	first_name=models.CharField(max_length=200)
# 	last_name=models.CharField(max_length=200)


# 	USERNAME_FIELD = 'email'
# 	REQUIRED_FIELDS = ['first_name','last_name']

# 	objects = CustomUserManager()
# 	class Meta:
# 		ordering = ["email"]
# 		verbose_name = "User"

# i need to talk allow me into the meet
