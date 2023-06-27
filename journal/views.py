from django.views.generic import CreateView, ListView, DetailView, DeleteView
from .models import Journal
import datetime
from .forms import JournalForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


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


class AddJournalPage(LoginRequiredMixin, CreateView):
    """
    Add a page to the journal
    """

    current_date = "MODNAYT"

    template_name = "journal/add_page.html"
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
