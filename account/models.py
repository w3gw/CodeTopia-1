from django.db import models

from django.conf import settings

from django.utils.translation import gettext_lazy as _


def get_profile_pic_path(instance, filename):
    """Method that returns upload location for the current user's profile picture"""
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    filename = instance.user, 's\'_profile_picure/%Y/%m/%d/'
    return 'user_', instance.user, '/', filename

class Profile(models.Model):

    class EducationBackground(models.TextChoices):
        PostGraduate = 'PostGraduate', _('PostGraduate')
        UnderGraduate = 'UnderGraduate', _('UnderGraduate')
        HighSchool = 'HighSchool', _('HighSchool')

    user = models.OneToOneField(
        to=settings.AUTH_USER_MODEL, 
        verbose_name=_("related_user"), 
        on_delete=models.CASCADE
    )
    profile_picture = models.ImageField(
        upload_to=get_profile_pic_path, 
        verbose_name=_("Profile Picture"), 
        height_field=300, 
        width_field=300, 
        max_length=100
    )

    education_background = models.CharField(
        verbose_name=_("Educational Background"), 
        choices=EducationBackground.choices, 
        max_length=30
    )

    phone_number_1 = models.CharField(verbose_name=_("First Phone Number"), max_length=13)
    phone_number_2 = models.CharField(
        verbose_name=_("Second Phone Number"), 
        max_length=13, null=True, blank=True
    )

    github_url = models.URLField(
        verbose_name=_('Github homepage URL.'), 
        max_length=150, blank=True, null=True
    )
    personal_url = models.URLField(
        verbose_name=_('Personal website URL.'), 
        max_length=150, blank=True, null=True
    )
    facebook_account = models.URLField(
        verbose_name=_('Facebook profile page.'), 
        max_length=255, blank=True, null=True
    )
    twitter_account = models.URLField(
        verbose_name=_('Twitter profile page.'), 
        max_length=255, blank=True, null=True
    )
    linkedin_account = models.URLField(
        verbose_name=_('LinkedIn profile page.'), 
        max_length=255, blank=True, null=True
    )

    short_bio = models.CharField(
        verbose_name=_('Describe yourself'), 
        max_length=60, blank=True, null=True
    )
    bio = models.CharField(
        verbose_name=_('Short bio'), 
        max_length=400, blank=True, null=True
    )

    def __str__(self):
        return "%s"% self.user.username