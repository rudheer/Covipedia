# Generated by Django 3.2 on 2021-05-23 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0005_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
