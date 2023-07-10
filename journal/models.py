from django.db import models
from django.contrib.auth.models import User
from django_currentuser.middleware import get_current_user
from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField
import datetime


class Journal(models.Model):
    """
    A model for each journal page entries
    """

    user = models.ForeignKey(
        User, related_name="journal_owner", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=30, null=False, blank=False)
    views = models.BigIntegerField(null=False, blank=False, default=0)
    content = RichTextField(max_length=15000, null=False, blank=False)
    journal_date = models.DateField(auto_now_add=True, null=False, blank=False)
    is_public = models.BooleanField(null=False, blank=False)
    self_image = ResizedImageField(
        size=[200, None],
        quality=80,
        upload_to="self_images/",
        force_format="WEBP",
        null=True,
        blank=True,
    )
    day_image = ResizedImageField(
        size=[800, None],
        quality=80,
        upload_to="day_images/",
        force_format="WEBP",
        null=True,
        blank=True,
    )

    def journalPageExistsForToday(self):
        """Check to see if there is already a page for this user today"""
        today = datetime.date.today()
        requestor = get_current_user()
        journal_page = Journal.objects.filter(
            journal_date=today,
            user=requestor
            )
        if journal_page:
            return journal_page[0].id
        else:
            return False

    def userHasFullProfile(self):
        """Check to see if this user has a full profile"""
        requestor = get_current_user()
        profile_match = Profile.objects.filter(
            user_id=requestor.id
            )
        if profile_match:
            return profile_match[0].user_id
        else:
            return False


    def addPageView(self):
        """
            Increase the total page views
        """
        self.views = self.views + 1
        self.save()
        return

    class Meta:
        ordering = ["-journal_date"]

    def __str__(self):
        return str(self.title)


class Profile(models.Model):
    """
    A model to manage users profile and settings
    """

    user = models.OneToOneField(
        User, related_name="account_user", on_delete=models.CASCADE
    )
    first_name = models.CharField(max_length=50, null=False, blank=True)
    last_name = models.CharField(max_length=50, null=False, blank=True)
    birthday = models.DateField(null=True, blank=True)
    account_activated = models.BooleanField(
        default=False,
        null=False,
        blank=False
        )
    make_new_page_public = models.BooleanField(
        default=False,
        null=False,
        blank=False
        )
    description_word_one = models.CharField(
        max_length=50,
        null=False,
        blank=True
        )
    description_word_two = models.CharField(
        max_length=50,
        null=False,
        blank=True
        )
    description_word_three = models.CharField(
        max_length=50,
        null=False,
        blank=True
        )
    colour_theme = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return str(self.id)


    def IsProfileComplete(self):
        """
            Has the user got an extended profile?
        """
        requestor = get_current_user()
        profile = Profile.objects.filter(
            user_id=requestor.id
            )
        if profile:
            return True
        else:
            return False
