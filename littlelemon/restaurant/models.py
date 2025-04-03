from django.db import models

# Create your models here.
class Booking(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    no_of_guests = models.IntegerField()
    bookingdate = models.DateField()
    
    def __str__(self):
        return self.name
    
class MenuItem(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.FloatField()
    inventory = models.IntegerField()
    
    def __str__(self):
        return self.title