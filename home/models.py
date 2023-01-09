from django.db import models


class Event(models.Model):
    event_name = models.CharField(max_length=280)
    date_start = models.DateField()
    date_end = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=280)
    description = models.TextField()

    class Meta:
        ordering = ('-date_start',)

    def __str__(self):
        return self.event_name
