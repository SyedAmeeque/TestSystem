# Generated by Django 5.0.7 on 2024-09-07 13:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0009_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='subject',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Test.subject'),
        ),
        migrations.AlterField(
            model_name='result',
            name='attempted_questions',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Test.subject'),
        ),
    ]
