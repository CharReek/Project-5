from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('post/edit/<int:pk>/<slug:slug>/', views.EditPostDetail.as_view(), name='edit_post'),
    path('post/delete/<int:pk>/<slug:slug>/', views.DeletePostDetail.as_view(), name='delete_post'),
]
