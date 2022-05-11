from pyexpat import model
from re import template
from statistics import mode
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Snack

class SnackListview(ListView):
    template_name = "snack_list.html"
    model = Snack
    contex_object_name = "snack_list"

class snackDetailView(DetailView):
    template_name = "snack_detail.html"
    model = Snack


