from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from blog.models import Post


class CreatePostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Post
        fields = ['author', 'title', 'slug', 'content', 'image', 'category']
        widgets = {
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'autocomplete': 'off',
                'id':'floatingAuthor',
                'placeholder': 'Автор статьи',
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'autocomplete': 'off',
                'id': 'floatingTitle',
                'placeholder': 'Заголовок',
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'floatingContent',
                'placeholder': 'Текст Статьи',
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'floatingSlug',
                'placeholder': 'URL',
            }),
            'category': forms.Select(attrs={
                'class': 'form-select',
                'autocomplete': 'off',
            }),
        }


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'