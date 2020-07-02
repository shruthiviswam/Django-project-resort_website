from django.db import models

# Create your models here.

class members(models.Model):
    title=models.CharField(max_length=10)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    username=models.CharField(max_length=50)
    gender=models.CharField(max_length=10,default='NA')
    date_of_birth=models.DateField()
    mail = models.EmailField()
    password=models.CharField(max_length=50)
    number = models.CharField(max_length=10)
    address=models.TextField()
    country=models.CharField(max_length=50)
    joindate = models.DateField()
    upload_file=models.FileField(upload_to="documents")

    class Meta:
        verbose_name_plural="Members"

    def __str__(self):
        return self.username

class EmployeeData(models.Model):
    name = models.CharField(max_length=10)
    dept = models.CharField(max_length=20)
    upload_file=models.FileField(upload_to="documents")

    class Meta:
        verbose_name_plural = 'Employee Images'

    def __str__(self):
        return self.name


class guest(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    name=models.CharField(max_length=20)
    mail=models.EmailField()
    phone=models.CharField(max_length=10)
    city=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    arrive=models.DateField()
    depart=models.DateField()
    people=models.IntegerField()
    room=models.CharField(max_length=10)
    bedding=models.CharField(max_length=10)
    comments=models.TextField()

    class Meta:
        verbose_name_plural="Guests"

    def __str__(self):
        return self.username