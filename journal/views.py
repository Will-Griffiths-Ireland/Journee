from django.views.generic import CreateView
from .models import Journal
from .forms import JournalForm
from django.contrib.auth.mixins import LoginRequiredMixin


class AddJournalPage(LoginRequiredMixin, CreateView):
    """
        Add a page to the journal
    """
    template_name = 'journal/add_page.html'
    model = Journal
    form_class = JournalForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddJournalPage, self).form_valid(form)
