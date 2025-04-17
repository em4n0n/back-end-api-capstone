from django.db import models

# Create your models here.
class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    no_of_guests = models.IntegerField()
    bookingdate = models.DateTimeField()
    
    class Meta:
        db_table = "booking"
    
class Menu(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    inventory = models.IntegerField()
    
    def __str__(self):
        return f'{self.title} : {str(self.price)}'
    
    class Meta:
        db_table = "menu"