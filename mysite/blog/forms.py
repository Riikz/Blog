from django import forms
from . import models
from django.views.generic.edit import UpdateView, DeleteView


class CreateBlog(forms.ModelForm):

    class Meta:
        model = models.Blog
        fields = ['blog_title', 'blog_body']


class EditBlogView(forms.ModelForm):

    class Meta:
        model = models.Blog
        fields = ['blog_title', 'blog_body']


class CreateComment(forms.ModelForm):

    class Meta:
        model = models.Comment
        fields = ['comment_body']
