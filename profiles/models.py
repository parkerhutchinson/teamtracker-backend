import datetime
from django.db import models
from django.utils.html import format_html
from django.conf import *


class Profiles(models.Model):
    ACCOUNT_MANAGEMENT = 'ACC'
    DEVELOPER = 'DEV'
    DESIGNER = 'DES'
    QUALITY_ASSURANCE = 'QUA'
    OPERATIONS = 'OPE'
    STRATEGY = 'STR'
    LEADERSHIP = 'LEA'
    TRAFFICING = 'TRA'
    DEVOPS = 'DPS'

    DEPARTMENTS = (
        (ACCOUNT_MANAGEMENT,'Account Management'),
        (DEVELOPER, 'Developer'),
        (DESIGNER, 'Designer'),
        (QUALITY_ASSURANCE, 'Quality Assurance'),
        (OPERATIONS, 'Operations'),
        (STRATEGY, 'Strategy'),
        (LEADERSHIP, 'Leadership'),
        (TRAFFICING, 'Trafficing'),
        (DEVOPS, 'IT & Devops'),
    )

    RED_TEAM = 'RED'
    BLUE_TEAM = 'BLU'
    YELLOW_TEAM = 'YEL'
    GREEN_TEAM = 'GRE'
    PURPLE_TEAM = 'PUR'
    GREY_TEAM = 'GRE'

    TEAMS = (
        (RED_TEAM, 'Red Team'),
        (BLUE_TEAM, 'Blue Team'),
        (YELLOW_TEAM, 'Yellow Team'),
        (GREEN_TEAM, 'Green Team'),
        (PURPLE_TEAM, 'Purple Team'),
        (GREY_TEAM, 'Grey Team'),
    )

    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    profile_image = models.ImageField(max_length=128, upload_to="profiles/")
    bio = models.TextField()
    department = models.CharField(max_length=3, choices=DEPARTMENTS)
    title = models.CharField(max_length=96)
    team_group = models.CharField(max_length=3, choices=TEAMS)
    twitter_handle = models.CharField(max_length=96, blank=True)
    overwatch_handle = models.CharField(max_length=96, blank=True)
    instagram_handle = models.CharField(max_length=96, blank=True)
    pinterest_handle = models.CharField(max_length=96, blank=True)
    steam_handle = models.CharField(max_length=96, blank=True)

    def __str__(self):
        return "{0}".format(self.email)

    def profile_image_inline(self):
        return format_html(
            '<img src="{}" width="400px"/>',
            '{0}{1}'.format('/files/', self.profile_image),
        )
