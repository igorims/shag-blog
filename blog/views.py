from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CreatePostForm
from .models import Post, Category
from .utils import DataMixin


class IndexView(DataMixin, ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    # extra_context = {'title': 'Главная страница'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context |= self.get_user_context(title='Главная страница') # updating context dictionary
        return context

    # def get_queryset(self):
    #     return Post.objects.filter(is_published=True)


class PostCreateView(LoginRequiredMixin, DataMixin, CreateView):
    form_class = CreatePostForm
    template_name = 'blog/create.html'
    raise_exception = True
    # login_url = reverse_lazy('blog:index') #  with LoginRequiredMixin, you can do this

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context |= self.get_user_context(title='Создание поста')  # updating context dictionary
        return context

    def handle_no_permission(self):
        return redirect('blog:index')

class PostDetailView(DataMixin, DetailView):
    model = Post
    template_name = 'blog/post-detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context |= self.get_user_context(title=f'{context["post"].title}')  # updating context dictionary
        return context

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post-delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('blog:index')

class CategoryView(DataMixin, ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context |= self.get_user_context(title=f'Категория {context["posts"][0].category.name}')  # updating context
        # dictionary
        return context

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['cat_slug'])


class RegisterUserView(DataMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'blog/register.html'
    success_url = reverse_lazy('blog:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context |= self.get_user_context(title='Регистрация')
        return context

    def form_valid(self, form):
        result = super().form_valid(form)
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
        )
        login(self.request, user)
        messages.add_message(
            message='Ура! Вы были зарегистрированы и залогинены!',
            request=self.request,
            level=messages.SUCCESS
        )

        return result

def logout_view(request):
    logout(request)
    return redirect('blog:index')

class UserProfileView(DataMixin,DetailView):
    model = User
    template_name = 'blog/user-detail.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context |= self.get_user_context(title='Профиль', categories=Category.objects.all())
        return context