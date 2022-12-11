from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# models = tables

class Pizza(models.Model):
    pizza_name = models.CharField(max_length=100)
    #added = models.DateTimeField(auto_now_add=True)    DO I NEED THIS?

    def __str__(self):
        return self.pizza_name

class Topping(models.Model):
    indiv_pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping_name = models.TextField(max_length=100)

    class Meta:
        verbose_name_plural = 'toppings'
    # he uses class meta to rename the website form entry to entries, but we don't need to do that

    def __str__(self):
        return self.topping_name



