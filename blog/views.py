"""
Этот модуль отвечает за обработку пользовательских запросов и отображение данных в приложении.
"""
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Post, User
from .forms import PostModelForm


def index(request):
    """
     Обрабатывает запросы к главной странице приложения.
    """
    return render(request, 'blog/base.html')


class PostListView(ListView):
    """Представление для отображения списка постов"""
    model = Post
    template_name = 'blog/list_for_post.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    """Представление для отображения деталей поста"""
    model = Post
    template_name = 'blog/detail_for_post.html'
    context_object_name = 'post'


class PostCreateView(CreateView):
    """Представление для создания нового поста"""
    model = Post
    template_name = 'blog/add_post.html'
    form_class = PostModelForm
    success_url = reverse_lazy("posts")

    def form_valid(self, form):
        messages.success(self.request, 'Пост успешно создан')
        return super().form_valid(form)


class PostDeleteView(DeleteView):
    """Представление для удаления поста"""
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('posts')


def user_list(request):
    """
    Представление для отображения списка пользователей.
    """
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'blog/users_list.html', context=context)


def user_posts(request, user_id):
    """
    Представление для отображения постов пользователей.
    """
    user = get_object_or_404(User, id=user_id)
    posts = Post.objects.filter(user=user)
    context = {
        'user': user,
        'posts': posts
    }
    return render(request, 'blog/users_posts.html', context=context)
