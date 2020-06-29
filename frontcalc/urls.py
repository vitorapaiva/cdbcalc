from django.urls import path
from . import views

urlpatterns = [
    path('', views.calc_form, name='calc_form'),
]