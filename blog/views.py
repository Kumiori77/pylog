from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from . import models
from . import forms

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
    

class PostAdd(FormView) :
    template_name = "post_add.html"

    form_class = forms.AddPostForm

    # success_url = reverse_lazy('blog:postList')

    posted_id = None

    def form_valid(self, form):

        form.save()

        self.posted_id = form.instance.id
        
        return super().form_valid(form)
    
    def get_success_url(self):
        # 요청 성공 후 이동할 postID와 페이지 반환

        success_url = reverse_lazy('blog:postDetail', kwargs={"post_id": self.posted_id})
   
        return success_url
    


        

