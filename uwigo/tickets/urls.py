from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='tickets'),
    path('create-ticket', views.create_ticket, name='create_ticket'),
]