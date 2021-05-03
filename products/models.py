from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=120)
    description = models.TextField()
    price       = models.DecimalField(max_digits=5,decimal_places=2)
    offer       = models.BooleanField()
    items       = models.IntegerField(default=2)

    def get_absolute_url(self):
        return reverse('product',kwargs={'id':self.id})       #f"/product/{self.id}/"
    def update(self):
        return reverse('update',kwargs={'id': self.id})
    