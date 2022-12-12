from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.db.models import Model

# Create your models here.
# models = tables

class Pizza(models.Model):
    pizza_name = models.CharField(max_length=100)
    #image_field = models.ImageField(null=True)

    def __str__(self):
        return self.pizza_name

class Topping(models.Model):
    indiv_pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping_name = models.TextField(max_length=100)

    def __str__(self):
        return self.topping_name

class Image(models.Model):
    indiv_image = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    image_field = models.ImageField(null=True)



#class Comment(models.Model):
#   post = models.ForeignKey(Pizza, on_delete=models.CASCADE)
#   text = models.CharField(max_length=200)
#   date_added = models.DateTimeField(auto_now_add=True,blank=True)
 
#   class Meta:
#       ordering = ('date_added',)
#
#   def __str__(self):
#       return self.text



