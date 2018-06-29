# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse

from core.models import User
from questions import views as quest_views
from django import forms
from django.views.generic import CreateView, UpdateView
from questions.models import Question

from .models import Comment

def comments_list(request, pk=None, qid=None):

    context = {}
    # context['comments'] = [
    #     {'cid': 1, 'name': 'Comment 1'},
    #     {'cid': 2, 'name': 'Comment 2'},
    #     {'cid': 3, 'name': 'Comment 3'},
    # ]
    # context['username'] = 'Alex'
    # context['category'] = {
    #     'id': pk
    # }
    # context['question'] = {
    #     'qid': qid
    # }
    context = {
        'comments': Comment.objects.all()
    }
    return render(request, 'comments/comments_list.html', context)

def comment_detail(request, pk=None, qid=None, cid=None):

    context = {}
    # context['comment'] = {
    #     'name': 'Comment',
    #     'cid': cid,
    # }
    # context['category'] = {
    #     'id': pk
    # }
    # context['question'] = {
    #     'qid': qid
    # }
    comment = Comment.objects.get(id=cid)

    context = {
        'comment': comment,
    }
    return render(request, 'comments/comment_detail.html', context)


# class CommentCreate(CreateView):
#
#     model = Comment
#     fields = 'text',
#     template_name = 'comments/comment_add.html'
#
#     def form_valid(self, form, cid=None):
#         form.instance.author = self.request.user
#         form.instance.question = self.request.question
#         return super(CommentCreate, self).form_valid(form)
#
#     def get_success_url(self):
#         return reverse('questions:question_detail', kwargs={'pk': self.object.question.categories.all()[:1].get().id, 'qid': self.object.question.id})
#
#
# class CommentEdit(UpdateView):
#
#     model = Comment
#     fields = 'text',
#     template_name = 'comments/comment_edit.html'
#
#     def get_queryset(self):
#         queryset = super(CommentEdit, self).get_queryset()
#         queryset = queryset.filter(author=self.request.user)
#         return queryset
#
#     def get_success_url(self):
#         return reverse('questions:question_detail', kwargs={'pk': self.object.question.categories.all()[:1].get().id, 'qid': self.object.question.id})

class CommentForm(forms.Form):

    comments_list = Comment.objects.all()
    text = forms.CharField(required=True, widget=forms.Textarea)


def comment_add(request, qid=None, pk=None):

    question = get_object_or_404(Question, id=qid)

    if request.method == 'GET':
        form = CommentForm()
        return render(request, 'comments/comment_add.html', {'form': form})
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if isinstance(request.user, User):
            if form.is_valid():
                data = form.cleaned_data
                comment = Comment(text=data['text'])
                comment.author = request.user
                comment.question = question
                comment.save()
                return redirect('questions:question_detail', pk=pk, qid=qid)
            else:
                return render(request, 'comments/comment_add.html', {'form': form})
        else:
            return render(request, 'comments/comment_add.html', {'form': form})


def comment_edit(request, pk=None, qid=None, cid=None):

    comment = get_object_or_404(Comment, id=cid)

    if request.method == 'GET':
        form = CommentForm(initial={'text': comment.text})
        return render(request, 'comments/comment_edit.html', {'form': form, 'comment': comment})
    if request.method == 'POST':
        form = CommentForm(request.POST, initial={'text': comment.text})
        if form.is_valid():
            data = form.cleaned_data
            comment.text = data['text']
            comment.save()
            return redirect('questions:question_detail', pk=pk, qid=qid)
        else:
            return render(request, 'comments/comment_edit.html', {'form': form, 'comment': comment})