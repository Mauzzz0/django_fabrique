# Generated by Django 2.2.10 on 2021-02-09 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0007_auto_20210209_1645'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='quiz',
        ),
        migrations.AddField(
            model_name='question',
            name='var1',
            field=models.CharField(max_length=30, null=True, verbose_name='Вариант ответа1'),
        ),
        migrations.AddField(
            model_name='question',
            name='var2',
            field=models.CharField(max_length=30, null=True, verbose_name='Вариант ответа2'),
        ),
        migrations.AddField(
            model_name='question',
            name='var3',
            field=models.CharField(max_length=30, null=True, verbose_name='Вариант ответа3'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='q1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quiz_q1', to='questionnaire.Question', verbose_name='Вопрос 1'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='q2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quiz_q2', to='questionnaire.Question', verbose_name='Вопрос 2'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='q3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quiz_q3', to='questionnaire.Question', verbose_name='Вопрос 3'),
        ),
    ]
