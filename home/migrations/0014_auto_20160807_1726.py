# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-07 17:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailforms', '0003_capitalizeverbose'),
        ('wagtailcore', '0028_merge'),
        ('wagtailredirects', '0005_capitalizeverbose'),
        ('home', '0013_auto_20160807_1708'),
    ]

    operations = [
        migrations.CreateModel(
            name='PeoplePageIndex',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('content', wagtail.wagtailcore.fields.StreamField([('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('people', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'name', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'position', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'biography', wagtail.wagtailcore.blocks.CharBlock()), (b'major', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'minor', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'grad_date', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'picture', wagtail.wagtailimages.blocks.ImageChooserBlock())])))])),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
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
