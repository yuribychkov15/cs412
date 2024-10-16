# mini_fb/views.py
# define the views for the mini_fb app
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView

from .models import * # import all of the models
from .forms import *

# class-based view 
# inherits from ListView
class ShowAllProfileViews(ListView):
    '''the view to show all profiles'''
    model = Profile
    template_name = "mini_fb/show_all_profiles.html"
    context_object_name = "profiles"


class ShowProfilePageView(DetailView):
    '''the view to show a single profile'''
    model = Profile
    template_name = "mini_fb/show_profile.html"
    context_object_name = "profile"

class CreateProfileView(CreateView):
    '''the view to create a single profile'''
    model = Profile
    form_class = CreateProfileForm
    template_name = "mini_fb/create_profile_form.html"

class CreateStatusMessageView(CreateView):
    '''the view to create a status message for a profile'''
    model = StatusMessage
    form_class = CreateStatusMessageForm
    template_name = "mini_fb/create_status_form.html"

    def get_context_data(self, **kwargs):
        # get context data from super class
        context = super().get_context_data(**kwargs)
        # find the Profile identified by the PK from the URL pattern
        profile = Profile.objects.get(pk=self.kwargs['pk'])
        # add Profile referred to by the URL into this context
        context['profile'] = profile
        return context
    
    def form_valid(self, form):
        # find Profile identified by the PK from the URL pattern
        profile = Profile.objects.get(pk=self.kwargs['pk'])
        # attach the Profile to the instance of the Message to set its FK
        form.instance.profile = profile
        # delefate work to superclass version of this method
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('show_profile', kwargs={'pk': self.kwargs['pk']})