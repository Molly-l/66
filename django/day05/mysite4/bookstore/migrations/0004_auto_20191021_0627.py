# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-10-21 06:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0003_auto_20191021_0615'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': '作者', 'verbose_name_plural': '作者'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': '图书', 'verbose_name_plural': '图书'},
        ),
        migrations.AlterModelTable(
            name='author',
            table='Author',
        ),
    ]