# mini_fb/views.py
# define the views for the mini_fb app
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import * # import all of the models

# class-based view 
# inherits from ListView
class ShowAllProfileViews(ListView):
    '''the view to show all profiles'''
    model = Profile
    template_name = "mini_fb/show_all_profiles.html"
    context_object_name = "profiles"