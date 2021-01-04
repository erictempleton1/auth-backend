from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.views.generic.base import TemplateView




class RegisterView(FormView):
  model = User
  form_class = UserCreationForm
  template_name = 'registration/create_user.html'
  success_url = 'accounts/profile/'

  def form_valid(self, form):
    user = form.save()
    login(self.request, user)
    return super().form_valid(form)


class ProfileView(TemplateView):
    template_name = "user/profile.html"
