from django.db import models

# Create your models here.
from userapp.models import User


class Article(models.Model):
    title = models.CharField("제목", max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField("글 내용")
    category = models.ManyToManyField("Category", verbose_name="카테고리")

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField("카테고리 제목", max_length=100)
    bio = models.CharField("설명", max_length=150)

    def __str__(self):
        return self.name
