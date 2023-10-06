from django.db import models


# Create your models here.

class Subject(models.Model):
    subject_name = models.CharField(max_length=200, blank=True)
    branch_choice = (
        ('Computer science and engineering', 'CSE'),
        ('Electrical engineering', 'EE'),
        ('Electronics and Communications Engineering', 'ECE'),
        ('Civil Engineering', 'CE'),
        ('Mechanical engineering', 'ME'),
    )
    year_choice = [
        (f'{i}',f'{i}') for i in range(1, 5)
    ]
    branch = models.CharField(choices=branch_choice, max_length=50, blank=True)
    year = models.CharField(choices=year_choice, max_length=50, blank=True)

    def __str__(self):
        return self.subject_name


class OldPaper(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, blank=True,null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    file=models.FileField(upload_to='OldPaper/file')
    year_choice = [
        (f'{i}',f'{i}') for i in range(2010, 2030)
    ]
    year = models.CharField(choices=year_choice, max_length=50, blank=True)
