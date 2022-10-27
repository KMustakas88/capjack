from django.db import models

class Customers(models.Model):

    _id = models.CharField(max_length=100, primary_key=True)
    created_at = models.BigIntegerField()
    updated_at = models.BigIntegerField()
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100, blank=True)
    world_viewable = models.BooleanField()

    def __str__(self):
        return self.name
