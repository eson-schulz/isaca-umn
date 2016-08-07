# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-07 16:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailforms', '0003_capitalizeverbose'),
        ('wagtailcore', '0028_merge'),
        ('wagtailredirects', '0005_capitalizeverbose'),
        ('wagtailimages', '0013_make_rendition_upload_callable'),
        ('home', '0011_personpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('biography', models.TextField(blank=True)),
                ('major', models.CharField(max_length=255)),
                ('minor', models.CharField(blank=True, max_length=255)),
                ('grad_date', models.CharField(max_length=255)),
                ('picture', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
        ),
        migrations.RemoveField(
            model_name='personpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='personpage',
            name='picture',
        ),
        migrations.DeleteModel(
            name='PersonPage',
        ),
    ]