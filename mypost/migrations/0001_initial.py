# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-25 01:04
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Biaoqian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('decs', ckeditor_uploader.fields.RichTextUploadingField()),
                ('content', models.TextField()),
                ('created', models.DateField(auto_now_add=True)),
                ('modified', models.DateField(auto_now=True)),
                ('biaoqian', models.ManyToManyField(to='mypost.Biaoqian')),
            ],
        ),
        migrations.CreateModel(
            name='Zhonglei',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='zhonglei',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mypost.Zhonglei'),
        ),
    ]
