# Generated by Django 4.0.5 on 2022-06-12 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assignmnet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='지역')),
            ],
        ),
        migrations.DeleteModel(
            name='Field',
        ),
        migrations.AlterField(
            model_name='enterpriseprofile',
            name='enterprise',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='assignmnet.enterprise', verbose_name='기업'),
        ),
        migrations.RemoveField(
            model_name='enterpriseprofile',
            name='place',
        ),
        migrations.AddField(
            model_name='enterpriseprofile',
            name='place',
            field=models.ManyToManyField(to='assignmnet.place', verbose_name='지역'),
        ),
    ]