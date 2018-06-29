# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.shortcuts import render, HttpResponse, render_to_response, redirect
from django.template.context_processors import csrf
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django import forms

# Create your views here.
from core.models import User


def start_page(request):

    return render(request, 'core/start_page.html')

def login(request):

    args ={}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/categories/')
        else:
            args['login_eror'] = "User not found"
            return render_to_response('core/login.html', args)
    else:
        return render_to_response('core/login.html', args)


def logout(request):

    auth.logout(request)
    return redirect('/categories/')


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields


def registration(request):
    args = {}
    args.update(csrf(request))
    args['form'] = CustomUserCreationForm()
    if request.POST:
        newuser_form = CustomUserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(
                username=newuser_form.cleaned_data['username'],
                password=newuser_form.cleaned_data['password2']
            )
            auth.login(request, newuser)
            return redirect('/categories/')
        else:
            args['form'] = newuser_form

    return render_to_response('core/registration.html', args)

