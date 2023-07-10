from django import forms
from django.contrib.auth.models import User
from django_currentuser.middleware import get_current_user
from djrichtextfield.widgets import RichTextWidget
from .models import Journal, Profile


class JournalForm(forms.ModelForm):
    """
        Form to enter a page in the journal
    """
    
    content = forms.CharField(widget=RichTextWidget())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_public'].initial = self.get_pub_pref()

    def get_pub_pref(self):
        user = get_current_user()
        if user.is_authenticated:
            try:
                profile = Profile.objects.get(user=user)
                return profile.make_new_page_public
            except Profile.DoesNotExist:
                return False
        return ""

    class Meta:
        model = Journal
        fields = ['title',
                  'content',
                  'is_public',
                  'self_image',
                  'day_image']

        labels = {
            'title': 'Title',
            'content': 'Journal Entry',
            'is_public': 'Share With Others?',
            'self_image': 'Selfie',
            'day_image': 'Photo Of The Day'
        }


class ProfileForm(forms.ModelForm):
    """
        Form to enter/edit profile details
    """
    class Meta:
        model = Profile
        fields = ['first_name',
                  'last_name',
                  'birthday',
                  'account_activated',
                  'make_new_page_public',
                  'description_word_one',
                  'description_word_two',
                  'description_word_three',
                  'colour_theme'
                  ]
        # labels = {
        #     'title': 'Title',
        #     'content': 'Journal Entry',
        #     'is_public': 'Share With Others?',
        #     'self_image': 'Selfie',
        #     'day_image': 'Photo Of The Day',
        #     'selected_theme': 'Theme'
        # }
