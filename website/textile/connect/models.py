# models.py

from django.contrib.auth.models import AbstractUser, User, Permission, Group
from django.db import models
from django.utils.translation import gettext_lazy as _
# from multiselectfield import MultiSelectField

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_owner = models.BooleanField(default=False)
    is_worker = models.BooleanField(default=False)

    groups = models.ManyToManyField(Group, verbose_name=_('groups'), blank=True, related_name='home_OwnerUser_groups')
    user_permissions = models.ManyToManyField(Permission, verbose_name=_('user permissions'), blank=True, related_name='home_OwnerUser_user_permissions')


class OwnerPublish(models.Model):
    INDUSTRIAL_PARK_CHOICES = [
        ('Bhagvati', 'Bhagvati'),
        ('Pramukh', 'Pramukh'),
        ('Sonal', 'Sonal'),
    ]

    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    industrial_park_name = models.CharField(max_length=20, choices=INDUSTRIAL_PARK_CHOICES)
    owner_name = models.CharField(max_length=100)
    firm_number = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=20)
    number_of_machines = models.PositiveIntegerField()
    requirement_bobin_checkbox = models.BooleanField(default=False)
    requirement_tfo_checkbox = models.BooleanField(default=False)
    requirement_karigar_checkbox = models.BooleanField(default=False)
    requirement_bobin = models.PositiveIntegerField(blank=True, null=True)
    requirement_tfo = models.PositiveIntegerField(blank=True, null=True)
    requirement_karigar = models.PositiveIntegerField(blank=True, null=True)
    submitted = models.BooleanField(default=False)


    def __str__(self):
        return self.owner_name


class WorkerProfile(models.Model):
    worker = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20)
    living_area = models.CharField(max_length=100)
    
    work_location_choices = [
        ('Bhagvati', 'Bhagvati'),
        ('Pramukh', 'Pramukh'),
        ('Sonal', 'Sonal'),
    ]
    work_location = models.CharField(max_length=20, choices=work_location_choices)

    area_of_work_choices = [
        ('Bobin', 'Bobin'),
        ('TFO', 'TFO'),
        ('Master', 'Master'),
    ]
    area_of_work = models.CharField(max_length=20, choices=area_of_work_choices)

    open_to_work = models.BooleanField(default=True)  # New field
    currently_working = models.BooleanField(default=False)

    def __str__(self):
        return self.name

