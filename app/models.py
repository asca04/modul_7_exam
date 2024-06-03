from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify


class Specialist(models.Model):
    name = models.CharField(max_length=50)


class Category(models.Model):
    name = models.CharField(max_length=50)


class District(models.Model):
    name = models.CharField(max_length=50)


class WorkTime(models.Model):
    name = models.CharField(max_length=50)


class User(AbstractUser):
    class Type(models.TextChoices):
        Employer = 'employer', 'Employer'
        Worker = 'Worker', 'worker'

    specialist = models.ManyToManyField(Specialist, )
    type = models.CharField(max_length=50, blank=True)
    seniority = models.IntegerField(blank=True, null=True)
    work_time = models.ForeignKey(WorkTime, on_delete=models.CASCADE, default=1)
    district = models.ForeignKey(District, on_delete=models.CASCADE, default=1)
    additional_info = models.TextField(blank=True)
    email = models.EmailField()

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        self.slug = slugify(self.email)
        super(User, self).save(*args, **kwargs)



class Vacancy(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=50)
    Company = models.CharField(max_length=100, null=True, blank=True)
    price = models.IntegerField(db_default=0, blank=True)
    location = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vacancies')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Vacancy, self).save(*args, **kwargs)
