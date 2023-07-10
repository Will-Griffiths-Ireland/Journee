from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Journal, Profile


class JournalForm(forms.ModelForm):
    """
        Form to enter a page in the journal
    """
    class Meta:
        model = Journal
        fields = ['title',
                  'content',
                  'is_public',
                  'self_image',
                  'day_image']
        
        content = forms.CharField(widget=RichTextWidget())

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
