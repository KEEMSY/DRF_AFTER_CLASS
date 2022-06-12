# Generated by Django 4.0.5 on 2022-06-09 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enterprise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100, verbose_name='기업 계정')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='이메일주소')),
                ('phone_number', models.IntegerField(verbose_name='담당자 전화번호')),
                ('fullname', models.CharField(max_length=20, verbose_name='이름')),
            ],
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='모집 분야')),
            ],
        ),
        migrations.CreateModel(
            name='EnterpriseProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('introduction', models.TextField()),
                ('place', models.CharField(max_length=100, verbose_name='근무지')),
                ('phone_number', models.IntegerField(verbose_name='기업 전화번호')),
                ('enterprise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignmnet.enterprise', verbose_name='기업명')),
            ],
        ),
    ]
