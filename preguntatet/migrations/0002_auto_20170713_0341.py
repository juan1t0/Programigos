# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-13 08:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preguntatet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregunta',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='respuesta',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]