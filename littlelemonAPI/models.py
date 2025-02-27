from django.db import models

# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    item_type = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.name

class ReservationItem(models.Model):
    name = models.CharField(max_length=100)
    partySize = models.IntegerField()
    time = models.DateTimeField()