from django.db import models
from django.contrib.auth.models import User
from django_currentuser.middleware import get_current_user
from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField
import datetime


class Journal(models.Model):
    """
    A model to create and manage journal page entries
    """

    user = models.ForeignKey(
        User, related_name="journal_owner", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=30, null=False, blank=False)
    content = RichTextField(max_length=15000, null=False, blank=False)
    journal_date = models.DateField(auto_now=True, null=False, blank=False)
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
    selected_theme = models.CharField(max_length=255, null=True, blank=True)

    def journalPageExistsForToday(self):
        """Check to see if there is already a page for this user today"""
        today = datetime.date.today()
        requestor = get_current_user()
        journal_page = Journal.objects.filter(journal_date=today, user=requestor)
        if journal_page:
            return journal_page[0].id
        else:
            return False


class Meta:
    ordering = ["-journal_date"]


def __str__(self):
    return str(self.title)
