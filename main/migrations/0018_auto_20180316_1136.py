# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-16 09:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_product_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.FileField(upload_to=''),
        ),
    ]