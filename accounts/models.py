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
    Father_name = models.CharField(max_length=100)
    Mother_name = models.CharField(max_length=100)

    username = None
    roll_number = models.CharField(max_length=100, unique=True)
    gender = models.CharField(max_length=20, choices=(('Male', 'Male'), ('Female', 'Female')))
    dob = models.DateField(default='1111-11-11')

    USERNAME_FIELD = 'roll_number'
    objects = User_manager()

    # Address
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    landmark = models.CharField(max_length=50)
    address = models.CharField(max_length=300)
    pincode = models.CharField(max_length=6)

    mobile_number = models.CharField(max_length=12)
    parent_mobile_number = models.CharField(max_length=12)
    adhar_number = models.CharField(max_length=20)
    marksheet_10 = models.FileField(upload_to='accounts/marksheet_10/',null=True)
    marksheet_12 = models.FileField(upload_to='accounts/marksheet_10/',null=True)
    profile = models.FileField(upload_to='accounts/profile/',null=True)
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
    branch=models.CharField(choices=branch_choice,max_length=50)
    batch=models.CharField(choices=batch_choice,max_length=50)

    def name(self):
        return self.first_name+' '+self.last_name
