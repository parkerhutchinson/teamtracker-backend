from django.db import models


class TimeTrackers(models.Model):
    name = models.CharField(max_length=96)
    description = models.CharField(max_length=2048)
    estimate = models.CharField(max_length=96)
    timer = models.DateTimeField()
    profile = models.ForeignKey('profiles.Profiles')
