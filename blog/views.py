from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from . import models

# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"

class PostList(TemplateView):
    template_name = "post_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        posts = models.Post.objects.all()

        context["posts"] = posts

        return context
    
class PostDetail(TemplateView):
    template_name = "post_detail.html"

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)

        post_id = self.kwargs['post_id']

        post = models.Post.objects.get(id=post_id)

        context["post"] = post

        return context

        

