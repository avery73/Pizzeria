from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    return render(request, 'pizzas/index.html')

def pizza_type(request):
    pizza_type = Pizza.objects.all()
    context = {'all_pizza_types':pizza_type}
    return render(request, 'pizzas/pizza_type.html', context)

def indiv_pizza(request, pizza_type_id):
    indiv_pizza = Pizza.objects.get(id=pizza_type_id)
    toppings = Topping.objects.filter(indiv_pizza=indiv_pizza)
    context = {'indiv_pizza':indiv_pizza, 'toppings':toppings}
    return render(request, 'pizzas/indiv_pizza.html', context)



