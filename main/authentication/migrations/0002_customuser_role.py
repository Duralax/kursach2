# Generated by Django 4.1.2 on 2022-11-17 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Manager'), (2, 'User')], default=2, verbose_name='role'),
        ),
    ]
