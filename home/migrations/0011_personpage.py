# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-07 16:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0028_merge'),
        ('wagtailimages', '0013_make_rendition_upload_callable'),
        ('home', '0010_auto_20160722_1841'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('biography', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('major', models.CharField(max_length=255)),
                ('minor', models.CharField(blank=True, max_length=255)),
                ('grad_date', models.CharField(max_length=255)),
                ('picture', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
