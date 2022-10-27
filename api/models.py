from django.db import models

from customers.models import Customers

class Segments(models.Model):

    _id = models.CharField(max_length=100, primary_key=True)
    created_at = models.BigIntegerField()
    updated_at = models.BigIntegerField()
    name = models.CharField(max_length=100)
    combines = models.CharField(max_length=100, blank=True)
    totalable = models.BooleanField()
    render = models.BooleanField()
    customer = models.ForeignKey(Customers,on_delete=models.CASCADE)
    # customer = models.CharField(max_length=100)

    def __str__(self):
        return self.name
