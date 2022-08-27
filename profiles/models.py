from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    a user profile model
    contains order history and delivery info
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=25, null=True, blank=True)
    default_street_address_1 = models.CharField(max_length=100, null=True, blank=True)
    default_street_address_2 = models.CharField(max_length=100, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=50, null=True, blank=True)
    default_county = models.CharField(max_length=100, null=True, blank=True)
    default_country = CountryField(blank_label='Country *', null=True, blank=True)
    default_postcode = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user(sender, instance, created, **kwargs):
    """ create or update a user profile """
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()
