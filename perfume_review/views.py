from django.views.generic import (
    CreateView, ListView,
    DetailView, DeleteView,
    UpdateView
)

from .models import Perfume
from .forms import PerfumeForm

from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)


class PerfumeDetail(DetailView):
    '''
    View one of the perfume reviews
    '''
    template_name = "perfume_review/perfume_detail.html"
    model = Perfume
    context_object_name = "perfume"


class Perfumes(ListView):
    '''
    View for all of the perfume reviews
    '''
    template_name = "perfume_review/perfumes.html"
    model = Perfume
    context_object_name = "perfumes"


class AddReview(CreateView):
    '''
    Add perfume review
    '''
    template_name = 'perfume_review/add_review.html'
    model = Perfume
    success_url = '/perfumes/'
    form_class = PerfumeForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddReview, self).form_valid(form)


class DeletePerfume(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    '''
    View to delete a perfume review
    '''
    model = Perfume
    success_url = '/perfumes/'

    def test_func(self):
        return self.request.user == self.get_object().user


class EditPerfume(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    '''
    View to edit a perfume review
    '''
    template_name = 'perfume_review/edit_perfume.html'
    model = Perfume
    form_class = PerfumeForm
    success_url = '/perfumes/'
    
    def test_func(self):
        return self.request.user == self.get_object().user