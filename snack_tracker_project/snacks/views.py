from msilib.schema import ListView
from pyexpat import model
from django.shortcuts import render
from django.views.generic import ListView
from .models import Snack

class SnackListview(ListView):
    template_name = "snack_list.html"
    model = Snack

