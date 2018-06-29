# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from questions import views as quest_views
from .models import Category
from django import forms


class CategoriesListForm(forms.Form):

    sort = forms.ChoiceField(choices=(
        ('name', 'Name asc'),
        ('-name', 'Name desc'),
        ('id', 'ID'),
    ), required=False)
    search = forms.CharField(required=False)



def categories_list(request):

    categories = Category.objects.all()

    form = CategoriesListForm(request.GET)
    if form.is_valid():
        data = form.cleaned_data
        if data['sort']:
            categories = categories.order_by(data['sort'])
        if data['search']:
            categories = categories.filter(name__icontains=data['search'])
    context = {
        'categories': categories,
        'categories_form': form,
    }
    return render(request, 'categories/categories_list.html', context)


class CategoryForm(forms.Form):

    name = forms.CharField(required=True)


def category_create(request):

    if request.method == 'GET':
        form = CategoryForm()
        return render(request, 'categories/category_create.html', {'form': form})
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            category = Category(name=data['name'])
            category.author = request.user
            category.save()
            return redirect('categories:category_detail', pk=category.id)
        else:
            return render(request, 'categories/category_create.html', {'form': form})


def category_edit(request, pk=None):

    category = get_object_or_404(Category, id=pk)

    if request.method == 'GET':
        form = CategoryForm(initial={'name': category.name})
        return render(request, 'categories/category_edit.html', {'form': form, 'category': category})
    if request.method == 'POST':
        form = CategoryForm(request.POST, initial={'name': category.name})
        if form.is_valid():
            data = form.cleaned_data
            category.name = data['name']
            category.save()
            return redirect('categories:category_detail', pk=category.pk)
        else:
            return render(request, 'categories/category_edit.html', {'form': form, 'category': category})


def category_detail(request, pk=None):

    category = get_object_or_404(Category, id=pk)

    context = {
        'category': category,
        'questions': category.questions.all().filter(is_archive=False)
    }
    return render(request, 'categories/category_detail.html', context)
