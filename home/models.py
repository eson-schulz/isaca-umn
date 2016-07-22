from __future__ import absolute_import, unicode_literals

from django.db import models
from django.db.models.fields import CharField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import StreamField, RichTextField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel


class HomePage(Page):
    header = CharField(max_length=200, blank=True)
    body = StreamField([
        ('paragraph', blocks.RichTextBlock()),
        ('video', EmbedBlock()),
    ], blank=True)
    background_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    content_panels = Page.content_panels + [
        FieldPanel('header'),
        StreamFieldPanel('body'),
        ImageChooserPanel('background_image')
    ]


class BlankPage(Page):
    body = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('body')
    ]


class ThinBlankPage(Page):
    body = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('body')
    ]