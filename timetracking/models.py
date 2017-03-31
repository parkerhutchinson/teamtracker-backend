from django.db import models


class TimeTrackers(models.Model):
    project_name = models.CharField(max_length=96)
    description = models.CharField(max_length=2048)
    estimate = models.CharField(max_length=96)
    timer = models.CharField(max_length=96)
    profile = models.ForeignKey('profiles.Profiles')
