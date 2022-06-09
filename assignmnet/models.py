from django.db import models


# Create your models here.
class Enterprise(models.Model):
    company_name = models.CharField("기업 계정", max_length=100)
    email = models.EmailField("이메일주소", max_length=100, unique=True)
    phone_number = models.IntegerField("담당자 전화번호")
    fullname = models.CharField("이름", max_length=20)


class EnterpriseProfile(models.Model):
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE, verbose_name='기업명')
    introduction = models.TextField()
    place = models.CharField("근무지", max_length=100)
    phone_number = models.IntegerField("기업 전화번호")


class Field(models.Model):
    name = models.CharField("모집 분야", max_length=100)
