from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


# Create your models here.
class User_manager(BaseUserManager):
    def create_superuser(self, roll_number, email='', password=None, **extra_fields):

        if not roll_number:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        user = self.model(
            roll_number=roll_number
        )
        user.set_password(password)

        user.email = email

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    Father_name = models.CharField(max_length=100,blank=True)
    Mother_name = models.CharField(max_length=100,blank=True)

    username = None
    roll_number = models.CharField(max_length=100, unique=True)
    gender = models.CharField(max_length=20, choices=(('Male', 'Male'), ('Female', 'Female')),blank=True)
    dob = models.DateField(null=True,blank=True)

    USERNAME_FIELD = 'roll_number'
    objects = User_manager()

    # Address
    country = models.CharField(max_length=50,blank=True)
    state = models.CharField(max_length=50,blank=True)
    city = models.CharField(max_length=50,blank=True)
    landmark = models.CharField(max_length=50,blank=True)
    address = models.CharField(max_length=300,blank=True)
    pincode = models.CharField(max_length=6,blank=True)

    mobile_number = models.CharField(max_length=12,blank=True)
    parent_mobile_number = models.CharField(max_length=12,blank=True)
    adhar_number = models.CharField(max_length=20,blank=True)
    marksheet_10 = models.FileField(upload_to='accounts/marksheet_10/',null=True,blank=True)
    marksheet_12 = models.FileField(upload_to='accounts/marksheet_10/',null=True,blank=True)
    profile = models.FileField(upload_to='accounts/profile/',null=True,blank=True)
    branch_choice=(
        ('Computer science and engineering', 'CSE'),
        ('Electrical engineering', 'EE'),
        ('Electronics and Communications Engineering', 'ECE'),
        ('Civil Engineering', 'CE'),
        ('Mechanical engineering', 'ME'),
    )
    batch_choice=[
        (f'{i}-{i+4}',f'{i}-{i+4}') for i in range(2019,2030)
    ]
    branch=models.CharField(choices=branch_choice,max_length=50,blank=True)
    batch=models.CharField(choices=batch_choice,max_length=50,blank=True)

    is_cr=models.BooleanField(default=False)
    def __str__(self):
        return self.name()

    def name(self):
        return self.first_name+' '+self.last_name
    def full_address(self):
        return f"{self.address} {self.landmark} {self.city} {self.state} {self.country} {self.pincode}"

class Superuser(User):
    class Meta:
        verbose_name = 'Superuser'
        verbose_name_plural = 'Superusers'
        proxy = True
class CR(User):
    class Meta:
        verbose_name = 'CR'
        verbose_name_plural = 'CRs'
        proxy = True
