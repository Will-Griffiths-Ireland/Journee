from django.urls import path
from .views import (
    AddJournalPage,
    Journals,
    ViewJournalPage,
    RemovePage,
    EditPage,
    JournalSearch,
    EditProfile,
    AddProfile,
    Showcase
    )

urlpatterns = [
    path("", Showcase.as_view(), name="showcase_journals"),
    path("add/", AddJournalPage.as_view(), name="add_journal_page"),
    path("journals/", Journals.as_view(), name="journals"),
    path("profile/", AddProfile.as_view(), name="add_profile"),
    path("profile/<slug:pk>/", EditProfile.as_view(), name="edit_profile"),
    path("search/journals/", JournalSearch.as_view(), name="journal_search"),
    path("journal/<slug:pk>/", ViewJournalPage.as_view(), name="view_journal_page"),
    path("delete/<slug:pk>/", RemovePage.as_view(),
         name="remove_journal_page"),
    path("edit/<slug:pk>/", EditPage.as_view(), name="edit_journal_page"),
]
