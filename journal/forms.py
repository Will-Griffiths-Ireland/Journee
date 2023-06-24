from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Journal


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
                  'day_image',
                  'selected_theme']
        
        content = forms.CharField(widget=RichTextWidget())

        labels = {
            'title': 'Title',
            'content': 'Journal Entry',
            'is_public': 'Share With Others?',
            'self_image': 'Selfie',
            'day_image': 'Photo Of The Day',
            'selected_theme': 'Theme'
        }
