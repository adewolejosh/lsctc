
from django.db import models
from django.contrib.auth import get_user_model

from .choices import GENDER


User = get_user_model()


class ProfileTimes(models.Model):
    created_time_and_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_time_and_date = models.DateTimeField(editable=True)

    class Meta:
        abstract = True


class SocialProfile(models.Model):
    twitter = models.CharField(max_length=100, blank=True, null=True)
    linkedin = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        abstract = True


class Profile(SocialProfile, ProfileTimes):
    user = models.ForeignKey(User, primary_key=True, on_delete=models.CASCADE)
    gender = models.TextField(choices=GENDER)
    occupation = models.CharField(max_length=100)
    next_of_kin = models.OneToOneField('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.user.firstname} {self.user.last_name}'
