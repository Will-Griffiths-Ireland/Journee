from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
)
from .models import Journal, Profile
import datetime
from .forms import JournalForm, ProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.db.models import Q


class Journals(ListView):
    """
    View all users journal pages
    """

    template_name = "journal/journals.html"
    model = Journal
    context_object_name = "journals"


class Showcase(ListView):
    """
    View public journals
    """

    template_name = "journal/showcase.html"
    model = Journal
    context_object_name = "journals"

    def get_queryset(self, **kwargs):
        journals = self.model.objects.filter(
                Q(is_public=True)
            ).order_by('-views')
        return journals


class ViewJournalPage(DetailView):
    """
    View a journal entry
    """

    template_name = "journal/view_page.html"
    model = Journal
    context_object_name = "journal_page"


class ViewProfilePage(DetailView):
    """
    View a users profile
    """

    template_name = "journal/view_profile.html"
    model = Profile
    context_object_name = "profile_page"


class JournalSearch(ListView):
    """
    View a journal entry
    """

    template_name = "journal/journal_search.html"
    model = Journal
    context_object_name = "journal_search"

    def get_queryset(self, **kwargs):
        query = self.request.GET.get("search_query")
        if query:
            journals = self.model.objects.filter(
                Q(is_public=True) &
                Q(content__icontains=query)
            )
        else:
            journals = self.model.objects.filter(
                Q(is_public=True)
            )
        return journals


class AddJournalPage(LoginRequiredMixin, CreateView, ListView, DetailView):
    """
    Add a page to the journal
    """

    template_name = "journal/add_page.html"
    context_object_name = "journals"
    model = Journal
    form_class = JournalForm
    success_url = "/journals/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddJournalPage, self).form_valid(form)


class RemovePage(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Remove Journal Page"""

    model = Journal
    success_url = "/journals/"

    def test_func(self):
        return self.request.user == self.get_object().user


class EditPage(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Update journal page"""

    template_name = "journal/edit_page.html"
    model = Journal
    form_class = JournalForm

    def get_success_url(self):
        return reverse_lazy("view_journal_page", kwargs={"pk": self.object.pk})

    def test_func(self):
        return self.request.user == self.get_object().user


class EditProfile(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Update user profile"""

    template_name = "journal/edit_profile.html"
    model = Profile
    form_class = ProfileForm
    success_url = "/journals/"

    def test_func(self):
        return self.request.user == self.get_object().user
    

class AddProfile(LoginRequiredMixin, CreateView):
    """
    Add a base profile
    """

    template_name = "journal/edit_profile.html"
    context_object_name = "add_profile"
    model = Profile
    form_class = ProfileForm
    success_url = "/journals/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddProfile, self).form_valid(form)