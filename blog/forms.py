from django import forms
from . import models

# 게시물 폼
class AddPostForm(forms.ModelForm):
    class Meta:
        model = models.Post

        fields = ["title", "content"]

        labels = {
            "title":"제목",
            "content":"내용 "
        }

# 댓글 폼
class AddCommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment

        fields = ["content"]

        labels = {
            "content":""
        }