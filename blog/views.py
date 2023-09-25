from typing import Any
from django.http import HttpResponse
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
    
class PostDetail(FormView):
    template_name = "post_detail.html"

    form_class = forms.AddCommentForm

    # 화면에 표시할 데이터 보내주기
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)

        self.post_id = self.kwargs['post_id']

        post = models.Post.objects.get(id=self.post_id)

        context["post"] = post

        return context
    # 폼이 전달되었을 때 처리
    def form_valid(self, form):
        post_id = self.kwargs["post_id"]

        post = models.Post.objects.get(id=post_id)

        form.instance.post = post
        form.save()

        return super().form_valid(form)
    
    # 성공 후 리다이렉트 url 지정
    def get_success_url(self):

        success_url = reverse_lazy('blog:postDetail', kwargs={"post_id": self.kwargs["post_id"]})

        return success_url
    


class PostAdd(FormView) :
    template_name = "post_add.html"

    form_class = forms.AddPostForm

    posted_id = None

    def form_valid(self, form):

        # 이미지 파일 받기
        thumbnail = form.cleaned_data["thumbnail"]

        form.instance.thumbnail = thumbnail

        form.save()

        self.posted_id = form.instance.id
        
        return super().form_valid(form)
    
    def get_success_url(self):
        # 요청 성공 후 이동할 postID와 페이지 반환

        success_url = reverse_lazy('blog:postDetail', kwargs={"post_id": self.posted_id})
   
        return success_url
    


        

