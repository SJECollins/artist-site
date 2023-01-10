from datetime import date
from django.db import models


class Event(models.Model):
    event_name = models.CharField(max_length=280, help_text='Name of event. Required.')
    date_start = models.DateField(help_text='Opening date of event. Required.')
    date_end = models.DateField(null=True, blank=True, help_text='End date of event. Optional.')
    location = models.CharField(max_length=280, help_text='Location of event. Does not accept linebreaks. Required.')
    description = models.TextField(help_text='Description of event. Accepts linebreaks. Required.')
    website = models.CharField(max_length=280, null=True, blank=True, help_text='Event website, enter full address for links. Optional.')
    website_name = models.CharField(max_length=280, null=True, blank=True, help_text='Name of website if website linked.')

    class Meta:
        ordering = ('-date_start',)

    def __str__(self):
        return self.event_name

    def get_upcoming(self):
        return self.date_start > date.today()

    def has_passed(self):
        if self.date_end:
            return self.date_end < date.today()
        else:
            return self.date_start < date.today()
