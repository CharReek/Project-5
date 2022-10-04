from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='blog_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('edit/<slug:slug>/', views.EditPostDetail.as_view(), name='edit_post'),
    path('delete/<slug:slug>/', views.DeletePostDetail.as_view(), name='delete_post'),
]
