from django.db import models

# Create your models here.
from userapp.models import User


class Event(models.Model):
    title = models.CharField("제목", max_length=100)
    thumbnail = models.ImageField("썸네일")
    explanation = models.CharField("설명", max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    effective_date = models.DateTimeField()
    expiration_date = models.DateTimeField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def change_active(self):
        self.active = not self.active
        self.save()


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    thumbnail = models.ImageField("썸네일")
    explanation = models.CharField("설명", max_length=256)
    price = models.IntegerField("가격")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expiration_date = models.DateTimeField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.explanation

    def change_active(self):
        self.active = not self.active
        self.save()


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    content = models.CharField("리뷰 내용", max_length=256)
    grade = models.IntegerField("평점")
    created_at = models.DateTimeField(auto_now_add=True)

