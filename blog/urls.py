from django.urls import path
from . import views
from .views import PostCreateView, PostDetailView, IndexView, PostDeleteView, CategoryView, RegisterUserView, \
    logout_view, UserProfileView
from django.contrib.auth import views as auth_views

app_name = 'blog'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('category/<slug:cat_slug>/', CategoryView.as_view(), name='category'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html', redirect_authenticated_user=True),
         name='login'),
    path('logout/', logout_view, name='logout'),

    path('user/<int:pk>/', UserProfileView.as_view(), name='user_detail')
]
