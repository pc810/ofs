# Generated by Django 2.1.5 on 2019-03-11 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0004_question_ques_option'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='ques_option',
            field=models.CharField(default='notspecified', max_length=500),
        ),
        migrations.AlterField(
            model_name='question',
            name='ques_text',
            field=models.CharField(default='notspecified', max_length=500),
        ),
    ]
