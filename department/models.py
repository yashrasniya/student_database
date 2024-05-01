from django.db import models
from accounts.models import User
from old_paper.models import Subject


# Create your models here.

class Image(models.Model):
    img = models.ImageField(upload_to='department_images', default='')




class Practical(models.Model):
    topic = models.TextField(max_length=2000, blank=True)
    description = models.TextField(max_length=2000, blank=True)


class Lab(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    about = models.TextField(max_length=20000, null=True, blank=True)
    hardware = models.TextField(max_length=20000, null=True, blank=True)
    practical = models.ManyToManyField(Practical,blank=True)


class Department(models.Model):
    branch_choice = (
        ('Computer science and engineering', 'CSE'),
        ('Electrical engineering', 'EE'),
        ('Electronics and Communications Engineering', 'ECE'),
        ('Civil Engineering', 'CE'),
        ('Mechanical engineering', 'ME'),
    )
    department_branch = models.CharField(choices=branch_choice, max_length=50, blank=True)
    department_subjects_name = models.ManyToManyField(Subject)
    department_labs_name = models.ManyToManyField(Lab)
    department_images = models.ManyToManyField(Image)
    deparment_faculty_HOD = models.ForeignKey(User, related_name='hod', on_delete=models.CASCADE)
    department_vision = models.TextField()
    department_objectives = models.TextField()
    department_description = models.TextField()
    department_mission = models.TextField()
    department_syllabus = models.FileField(upload_to='pdfs/', default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deparment_faculty = models.ManyToManyField(User, related_name='faculty_name')

    class Meta:
        verbose_name = ("Department")
        verbose_name_plural = ("Departments")

    def __str__(self):
        return self.department_branch

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


class NavBar(models.Model):
    title = models.CharField(max_length=50)
    link = models.URLField(max_length=2400)
    child = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children')


class Working_communities(models.Model):
    name = models.CharField(max_length=50)
    Faculty = models.ForeignKey(User, on_delete=models.CASCADE, related_name='working_communities')

    def __str__(self):
        return self.name



