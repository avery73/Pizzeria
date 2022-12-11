from django.urls import path

from . import views

app_name = 'pizzas'

urlpatterns = [
    path('',views.index,name='index'),
    path('pizza_type',views.pizza_type,name='pizza_type'),
    path('pizza_type/<int:pizza_type_id>/',views.indiv_pizza,name='indiv_pizza'),
]