# Generated by Django 5.0.7 on 2024-08-22 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0007_alter_result_result_paper_delete_paper_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='actual_answer',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='questions',
            name='option_a',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='questions',
            name='option_b',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='questions',
            name='option_c',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='questions',
            name='option_d',
            field=models.CharField(max_length=200),
        ),
    ]
