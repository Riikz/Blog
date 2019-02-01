from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect


class Blog(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_liked = models.BooleanField(default=False)

    def __str__(self):
        return self.blog_title

    def get_absolute_url(self):
        return HttpResponseRedirect(reverse('blog:index'))


class Comment(models.Model):
    comment_body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_body
