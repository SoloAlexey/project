# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import request
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from django import forms
from django.views.generic import CreateView, UpdateView, DetailView

from core.models import User
from .models import Question
from categories.models import Category

def questions_list(request, pk=None):

    context = {}
    # context['questions'] = [
    #     {'qid': 1, 'name': 'Question 1'},
    #     {'qid': 2, 'name': 'Question 2'},
    #     {'qid': 3, 'name': 'Question 3'},
    # ]
    # context['username'] = 'Alex'
    # context['category'] = {
    #     'id': pk
    # }

    context = {
        'catid': pk,
        'questions': Question.objects.all()
    }
    return render(request, 'questions/questions_list.html', context)


def question_detail(request, pk=None, qid=None):

    # context = {}
    # context['question'] = {
    #     'name': 'Question',
    #     'qid': qid,
    # }
    # context['category'] = {
    #     'id': pk
    # }
    question = Question.objects.get(id=qid)

    context = {
        'catid': pk,
        'question': question,
        'comments': question.comments.all().filter(is_archive=False)
    }
    return render(request, 'questions/question_detail.html', context)


# class QuestionForm(forms.Form):
#
#     categories_list = Category.objects.name
#
#     name = forms.CharField(required=True)
#     text = forms.CharField(required=True, widget=forms.Textarea)
#     #categories = forms.ChoiceField(initial=categories_list)


class QuestionCreate(CreateView):

    model = Question
    fields = 'name', 'text', 'categories'
    template_name = 'questions/question_create.html'

    def form_valid(self, form):
        if isinstance(self.request.user, User):
            form.instance.author = self.request.user
            return super(QuestionCreate, self).form_valid(form)
        else:
            return super(QuestionCreate, self).form_invalid(form)


    def get_success_url(self):
        return reverse('questions:question_detail', kwargs={'qid': self.object.pk, 'pk': self.object.categories.all()[:1].get().id})


class QuestionEdit(UpdateView):

    model = Question
    fields = 'name', 'text', 'categories'
    template_name = 'questions/question_edit.html'
    pk_url_kwarg = 'qid'


    def get_queryset(self):
        queryset = super(QuestionEdit, self).get_queryset()
        queryset = queryset.filter(author=self.request.user)
        return queryset


    def get_success_url(self):
        return reverse('questions:question_detail', kwargs={'qid': self.object.pk, 'pk': self.object.categories.all()[:1].get().id})

class CommentsView(DetailView):

    queryset = Question.objects.all()
    template_name = 'questions/comments.html'


# def question_create(request, pk=None):
#
#     category = get_object_or_404(Category, id=pk)
#
#     if request.method == 'GET':
#         form = QuestionForm()
#         return render(request, 'questions/question_create.html', {'form': form})
#     if request.method == 'POST':
#         form = QuestionForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             question = Question(name=data['name'], text=data['text'])
#             question.author = request.user
#             question.save()
#             question.categories = {category}
#             question.save()
#             return redirect('questions:question_detail', pk=pk, qid=question.id)
#         else:
#             return render(request, 'questions/question_create.html', {'form': form})
#
#
# def question_edit(request, pk=None, qid=None):
#
#     question = get_object_or_404(Question, id=qid)
#
#     if request.method == 'GET':
#         form = QuestionForm(initial={'name': question.name, 'text': question.text})
#         return render(request, 'questions/question_edit.html', {'form': form, 'question': question})
#     if request.method == 'POST':
#         form = QuestionForm(request.POST, initial={'name': question.name, 'text': question.text})
#         if form.is_valid():
#             data = form.cleaned_data
#             question.name = data['name']
#             question.text = data['text']
#             question.categories = data['categories']
#             question.save()
#             return redirect('questions:question_detail', pk=pk, qid=question.pk)
#         else:
#              return render(request, 'questions/question_edit.html', {'form': form, 'question': question})