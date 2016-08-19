from __future__ import absolute_import, unicode_literals

from django.db import models
from django.db.models.fields import CharField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import StreamField, RichTextField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel


class CalendarBlock(blocks.StructBlock):
    url = blocks.CharBlock(required=True)

    class Meta:
        icon = 'date'
        template = 'home/blocks/calendar.html'

    def __unicode__(self):
        return self.url


# Block used to subscribe users to a MailChimp account
class EmailBlock(blocks.StructBlock):
    action_url = blocks.CharBlock(required=True)
    hidden_field_name = blocks.CharBlock(required=True)

    class Meta:
        icon = 'mail'
        template = 'home/blocks/email.html'

    def __unicode__(self):
        return self.action_url


class PersonBlock(blocks.StructBlock):
    name = blocks.CharBlock(required=True)
    position = blocks.CharBlock(required=True)
    biography = blocks.CharBlock(required=False)

    major = blocks.CharBlock(required=True)
    minor = blocks.CharBlock(required=False)
    grad_date = blocks.CharBlock(required=True)

    picture = ImageChooserBlock(required=False)

    class Meta:
        icon = 'user'
        template = 'home/blocks/person.html'

    def __unicode__(self):
        return self.name


# Used for settings the default Streamfield
class DefaultBlock(blocks.StreamBlock):
    paragraph = blocks.RichTextBlock()
    calendar = CalendarBlock()
    mailchimp = EmailBlock()
    person_list = blocks.ListBlock(PersonBlock(), template='home/blocks/person_list.html', icon='user')


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
    body = StreamField(DefaultBlock())

    content_panels = Page.content_panels + [
        StreamFieldPanel('body')
    ]


class ThinBlankPage(Page):
    body = StreamField(DefaultBlock())

    content_panels = Page.content_panels + [
        StreamFieldPanel('body')
    ]