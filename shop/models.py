from django.db import models

# Create your models here.

class Part(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    img = models.ImageField(blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=40)

    class Meta:
        ordering = ['created']

