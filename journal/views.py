from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
)
from .models import Journal
import datetime
from .forms import JournalForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy


class Journals(ListView):
    """
    View all users journal pages
    """

    template_name = "journal/journals.html"
    model = Journal
    context_object_name = "journals"


class ViewJournalPage(DetailView):
    """
    View a journal entry
    """

    template_name = "journal/view_page.html"
    model = Journal
    context_object_name = "journal_page"


class AddJournalPage(LoginRequiredMixin, CreateView, ListView, DetailView):
    """
    Add a page to the journal
    """

    template_name = "journal/add_page.html"
    context_object_name = "journals"
    model = Journal
    form_class = JournalForm
    success_url = "/journal/journals/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddJournalPage, self).form_valid(form)


class RemovePage(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Remove Journal Page"""

    model = Journal
    success_url = "/journal/journals/"

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
