"""
Этот модуль отвечает за маршрутизацию URL в приложении.
"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='base'),
    path('posts/', views.PostListView.as_view(), name='posts'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='detail_for_post'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete_post'),
    path('posts/add/', views.PostCreateView.as_view(), name='add_post'),
    path('users/', views.user_list, name='users'),
    path('users/<int:user_id>/', views.user_posts, name='user_posts'),
]
