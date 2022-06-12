from django.db import models


# Create your models here.


class Enterprise(models.Model):
    company_name = models.CharField("기업 계정", max_length=100)
    email = models.EmailField("이메일주소", max_length=100, unique=True)
    phone_number = models.IntegerField("담당자 전화번호")
    fullname = models.CharField("이름", max_length=20)


class EnterpriseProfile(models.Model):
    enterprise = models.OneToOneField(to=Enterprise, verbose_name="기업", on_delete=models.CASCADE)
    introduction = models.TextField()
    place = models.ManyToManyField(to="Place", verbose_name='지역')
    phone_number = models.IntegerField("기업 전화번호")


class Place(models.Model):
    name = models.CharField("지역", max_length=50)
