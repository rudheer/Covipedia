# Generated by Django 3.2 on 2021-07-06 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0008_blog_downchek'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='downchek',
            field=models.BooleanField(verbose_name=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='upchek',
            field=models.BooleanField(verbose_name=True),
        ),
    ]