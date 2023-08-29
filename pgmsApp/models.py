from django.db import models

# Create your models here.
class Occupant(models.Model):
    ROOM_TYPE = [('single','Single'),('double','Double'),('triple','Triple')]
    OCCUPATION = [('student','Student'),('employee','Employee'),('other','Other')]
    name = models.CharField(max_length=30)
    occupation = models.CharField(max_length=20,choices=OCCUPATION)
    roomType = models.CharField(max_length=10,choices=ROOM_TYPE)
    entryDate = models.DateField()
    
class ElectricityBill(models.Model):
    
    exit = models.DateField()
    days = models.IntegerField()
    occupant = models.OneToOneField(Occupant,on_delete=models.CASCADE)
    