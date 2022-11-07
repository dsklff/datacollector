# Generated by Django 3.1.2 on 2020-11-09 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='kbtumail',
        ),
        migrations.AddField(
            model_name='teacher',
            name='full_name',
            field=models.CharField(default='Damir', max_length=100),
        ),
        migrations.AddField(
            model_name='teacher',
            name='kbtu_mail',
            field=models.EmailField(default='user1@kbtu.kz', max_length=255, unique=True),
        ),
    ]