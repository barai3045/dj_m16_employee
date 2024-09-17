from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Employee(models.Model):

    DESIGNATIONS = [
        ('Manager', 'Manager'),
        ('Team Lead', 'Team Lead'),
        ('Developer', 'Developer'),
        ('Tester', 'Tester'),
        ('HR', 'HR'),
    ]

    emp_id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=12)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    designation = models.CharField(max_length=50,choices=DESIGNATIONS)
    short_description = models.TextField()
    user=models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.emp_id}: {self.name}"