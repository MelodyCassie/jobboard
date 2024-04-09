from django.db import models


# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    company_name = models.CharField(max_length=100)
    requirements = models.TextField()
    salary = models.BigIntegerField()
    location = models.ForeignKey('Location', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} {self.description} {self.company_name} {self.requirements} {self.salary} {self.location}'


class Location(models.Model):
    country = models.CharField(max_length=150)
    state = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.country} {self.state}'


