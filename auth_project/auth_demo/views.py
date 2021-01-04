from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User


class RegisterView(CreateView):
  model = User
  form_class = UserCreationForm
  template_name_suffix = '_create_form'
