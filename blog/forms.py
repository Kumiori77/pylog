from django import forms
from . import models

# 애완 동물 추가 폼
class AddPostForm(forms.ModelForm):
    class Meta:
        model = models.Post

        fields = ["title", "content"]

        labels = {
            "title":"제목",
            "content":"내용 "
        }