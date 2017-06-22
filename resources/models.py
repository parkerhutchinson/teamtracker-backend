from django.db import models
from django.conf import *
from django.core.files.storage import FileSystemStorage


class Resources(models.Model):
    # resource types
    LINK = 'LNK'
    FILE = 'FLE'

    # sow child
    CONSULTING_AGREEMENT = 'CAG'
    FACILITY_AGREEMENT = 'FAG'  # what do I do here?
    MASTER_AGREEMENT = 'MAG'
    NONDISCLOSURE_AGREEMENT = 'NAG'

    # process child
    KICK_OFF = 'KOF'
    DEVELOPMENT = 'DEV'
    LAUNCH = 'LAU'
    SUPPORT = 'SUP'
    TEAMS = 'TEA'
    SALES = 'SAL'

    # marketing child
    ONE_SHEET = 'OSH'
    PITCH_DECK = 'PDE'
    PROPOSALS = 'PRO'

    # brand child
    ASSETS = 'ASS'  # don't blame me if you have a problem with my naming conventions
    STYLE_GUIDE = 'SGU'
    TEMPLATES = 'TEM'

    # other & HR
    OTHER = 'OTH'

    RESOURCES_GROUP = ([
        ('Statement of Work / Legal', [
            (CONSULTING_AGREEMENT, 'Consulting Services Agreement'),
            (FACILITY_AGREEMENT, 'Facility License Agreement'),
            (MASTER_AGREEMENT, 'Master Services Agreement'),
            (NONDISCLOSURE_AGREEMENT, 'Non-Disclosure Agreement (NDA)'),
            (OTHER, 'Other'),
         ]),
        ('Project Process', [
            (KICK_OFF, 'Kick Off'),
            (DEVELOPMENT, 'Development'),
            (LAUNCH, 'Launch'),
            (SUPPORT, 'Support'),
            (TEAMS, 'Teams'),
            (OTHER, 'Other'),
         ]),
        ('Sales / Marketing', [
            (ONE_SHEET, 'One-Sheets'),
            (PITCH_DECK, 'Pitch / Capabilities Decks'),
            (PROPOSALS, 'Proposals'),
            (OTHER, 'Other'),
         ]),
        ('PRPL Brand', [
            (ASSETS, 'Assets'),
            (STYLE_GUIDE, 'Style Guides'),
            (TEMPLATES, 'Templates'),
            (OTHER, 'Other'),
         ]),
        ('HR & Paperwork', [
            (OTHER, 'Other'),
         ]),
    ])

    RESOURCE_TYPE = (
        (LINK, 'Link'),
        (FILE, 'File'),
    )

    name = models.CharField(max_length=1024)
    type = models.CharField(max_length=3, choices=RESOURCE_TYPE)
    file = models.FileField(
        storage=FileSystemStorage(location=settings.MEDIA_ROOT),
        upload_to='resources/',
        null=True,
        blank=True,
    )
    url = models.CharField(max_length=1024, blank=True)
    resources_group = models.CharField(max_length=3, choices=RESOURCES_GROUP, blank=True)
    profile = models.ForeignKey('profiles.profiles', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

