# Generated by Django 3.1.2 on 2020-11-10 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_remove_teacher_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='full_name',
            field=models.CharField(default='Damir', max_length=100),
        ),
    ]