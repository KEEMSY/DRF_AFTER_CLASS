from django.db import models


# Create your models here.

class Event(models.Model):
    title = models.CharField("제목", max_length=100)
    thumbnail = models.ImageField("썸네일")
    explanation = models.CharField("설명", max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    effective_data = models.DateTimeField()
    expiration_data = models.DateTimeField()
    active = models.BooleanField()

    def __str__(self):
        return self.title

    def change_active(self):
        self.active = not self.active
        self.save()