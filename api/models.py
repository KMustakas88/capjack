from django.db import models

class Segments(models.Model):

    _id = models.CharField(max_length=100, primary_key=True)
    created_at = models.BigIntegerField()
    updated_at = models.BigIntegerField()
    name = models.CharField(max_length=100)
    combines = models.CharField(max_length=100)
    totalable = models.BooleanField()
    render = models.BooleanField()
    customer = models.CharField(max_length=100)

    def __str__(self):
        return self.name
