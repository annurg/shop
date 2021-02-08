from django.db import models
from django.contrib.auth.models import User
import decimal


class Person(models.Model):
    name = models.CharField(max_length=50, unique=True)
    phone = models.IntegerField(unique=True, default=None)
    paid = models.DecimalField(max_digits=10, decimal_places=1, default=0)

    def __str__(self):
        return self.name

class Record(models.Model):
    date = models.DateTimeField()
    total_amount = models.DecimalField(max_digits=10,decimal_places=1, editable=False, null=True)
    user = models.ForeignKey(to=Person, on_delete=models.CASCADE, default=None)

    def person(self):
        return self.user.name

    def __str__(self):
        return self.date.strftime("%d-%m-%Y")

class Item(models.Model):
    record = models.ForeignKey(to=Record, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=30,)
    price = models.DecimalField(max_digits=10, decimal_places=1)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return '({} , {}, {})'.format(self.name, self.price, self.quantity)
    
 
