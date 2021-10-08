from django.utils.text import slugify
from unidecode import unidecode

from django.db import models
from django.forms import forms
from django.urls import reverse
from PIL import Image


class Post(models.Model):
    author = models.CharField("Автор статьи", max_length=100)
    title = models.CharField("Название статьи", max_length=100)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL', blank=True, null=True)
    content = models.TextField("Текст статьи")
    image = models.ImageField('Картинка к посту', upload_to='img', null=True, blank=True)
    publish_date = models.DateTimeField("Время публикации", auto_now_add=True)
    is_published = models.BooleanField('Пост опубликован?', default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug' : self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            string = str(self.title)
            self.slug = slugify(unidecode(string))
        return super().save()

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField('Категория',max_length=30, unique=True)
    slug = models.SlugField('URL', max_length=30, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:category', kwargs={'cat_slug' : self.slug})
