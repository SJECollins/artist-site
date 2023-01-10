from datetime import date
from django.db import models


class Event(models.Model):
    event_name = models.CharField(max_length=280)
    date_start = models.DateField()
    date_end = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=280)
    description = models.TextField()
    website = models.CharField(max_length=280, null=True, blank=True)
    website_name = models.CharField(max_length=280, null=True, blank=True)

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
