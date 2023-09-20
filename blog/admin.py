from django.contrib import admin
from blog import models

# Register your models here.

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "thumbnail"]


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    pass