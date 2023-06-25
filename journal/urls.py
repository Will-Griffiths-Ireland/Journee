from django.urls import path
from .views import AddJournalPage, Journals, ViewJournalPage


urlpatterns = [
    path("", AddJournalPage.as_view(), name="add_journal_page"),
    path("journals/", Journals.as_view(), name="journals"),
    path("<slug:pk>/", ViewJournalPage.as_view(), name="view_journal_page"),
]
