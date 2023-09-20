from django.urls import path
from . import views
from blog import views

# 유저가 업로드한 파일을 보기위한 설정
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("posts/", views.PostList.as_view(), name="postList"),
    path("posts/<int:post_id>/", views.PostDetail.as_view(), name="postDetail"),
]

# 유저가 업로드한 파일을 보기위한 설정
urlpatterns += static(
    prefix=settings.MEDIA_URL,
    document_root = settings.MEDIA_ROOT,
)

app_name = "blog"
