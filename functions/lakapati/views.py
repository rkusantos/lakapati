from atexit import register
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django import template
from django.contrib.auth.models import Group
from django.shortcuts import render
import os

register = template.Library()

class HomePage(LoginRequiredMixin, TemplateView):

    template_name = 'index.html'
    @register.filter(name='is_group')
    def is_group(user, group_name, request):
        group = Group.objects.get(name = group_name)
        return group in user.groups.all()
       

    login_url = 'accounts/login/'
    