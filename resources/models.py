import datetime
from django.utils import timezone
from django.db import models


class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return datetime.datetime.now()


class Resources(models.Model):
    STATEMENT_OF_WORK = 'SOW'
    PROCESS = 'PRO'
    SALES_MARKETING = 'SAL'
    PRPL_BRAND = 'BRA'
    HR_PAPERWORK = 'HRP'

    GROUP = (
        (STATEMENT_OF_WORK, 'Statement of Work / Legal'),
        (PROCESS, 'Project Process'),
        (SALES_MARKETING, 'Sales / Marketing'),
        (PRPL_BRAND, 'PRPL Brand'),
        (HR_PAPERWORK, 'HR & Paperwork'),
    )

    group = models.CharField(max_length=3, choices=GROUP)
    filename = models.CharField(max_length=1024)
    profile = models.ForeignKey('profiles.profiles')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
