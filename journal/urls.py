from django.urls import path
from .views import AddJournalPage


urlpatterns = [
    path('', AddJournalPage.as_view(), name='add_journal_page'),
]