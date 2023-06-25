from django.urls import path
from .views import AddJournalPage, Journals


urlpatterns = [
    path("", AddJournalPage.as_view(), name="add_journal_page"),
    path("journals/", Journals.as_view(), name="journals"),
]
