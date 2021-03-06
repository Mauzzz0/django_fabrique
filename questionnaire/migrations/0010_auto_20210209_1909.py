# Generated by Django 2.2.10 on 2021-02-09 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0009_completedquiz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completedquiz',
            name='q1',
            field=models.CharField(blank=True, max_length=255, verbose_name='Вопрос1'),
        ),
        migrations.AlterField(
            model_name='completedquiz',
            name='q1ans',
            field=models.CharField(blank=True, max_length=255, verbose_name='Ответ на вопрос1'),
        ),
        migrations.AlterField(
            model_name='completedquiz',
            name='q2',
            field=models.CharField(blank=True, max_length=255, verbose_name='Вопрос2'),
        ),
        migrations.AlterField(
            model_name='completedquiz',
            name='q2ans',
            field=models.CharField(blank=True, max_length=255, verbose_name='Ответ на вопрос2'),
        ),
        migrations.AlterField(
            model_name='completedquiz',
            name='q3',
            field=models.CharField(blank=True, max_length=255, verbose_name='Вопрос3'),
        ),
        migrations.AlterField(
            model_name='completedquiz',
            name='q3ans',
            field=models.CharField(blank=True, max_length=255, verbose_name='Ответ на вопрос3'),
        ),
    ]
