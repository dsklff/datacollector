# Generated by Django 3.1.3 on 2021-01-13 13:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('discipline', '0002_discipline_credit_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discipline',
            name='teacher',
        ),
        migrations.AddField(
            model_name='discipline',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='endterm',
            name='discipline',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='endterms', to='discipline.discipline'),
        ),
        migrations.AlterField(
            model_name='final',
            name='discipline',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='finals', to='discipline.discipline'),
        ),
        migrations.AlterField(
            model_name='laboratorywork',
            name='discipline',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='labworks', to='discipline.discipline'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='discipline',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lectures', to='discipline.discipline'),
        ),
        migrations.AlterField(
            model_name='midterm',
            name='discipline',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='midterms', to='discipline.discipline'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='discipline',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quizes', to='discipline.discipline'),
        ),
        migrations.AlterField(
            model_name='sis',
            name='discipline',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sises', to='discipline.discipline'),
        ),
        migrations.AlterField(
            model_name='syllabus',
            name='discipline',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='syllabuses', to='discipline.discipline'),
        ),
        migrations.AlterField(
            model_name='tsis',
            name='discipline',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tsises', to='discipline.discipline'),
        ),
    ]
