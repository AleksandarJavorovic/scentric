from django.views.generic import (
    CreateView, ListView,
    DetailView, DeleteView,
    UpdateView
)

from django.contrib import messages

from .models import Perfume
from .forms import PerfumeForm

from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)

from django.contrib.messages.views import SuccessMessageMixin

from django.db.models import Q


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

    def get_queryset(self, **kwargs):
        query = self.request.GET.get('q')
        if query:
            perfumes = self.model.objects.filter(
                Q(perfume_brand__icontains=query) |
                Q(perfume_name__icontains=query) |
                Q(perfume_group__icontains=query) |
                Q(concentration__icontains=query) |
                Q(top_notes__icontains=query) |
                Q(middle_notes__icontains=query) |
                Q(base_notes__icontains=query)
            )
        else:
            perfumes = self.model.objects.all()
        return perfumes


class AddReview(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    '''
    Add perfume review
    '''
    template_name = 'perfume_review/add_review.html'
    model = Perfume
    success_url = '/perfumes/'
    form_class = PerfumeForm
    success_message = 'Perfume Review has been successfully created!'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddReview, self).form_valid(form)


class DeletePerfume(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    '''
    View to delete a perfume review
    '''
    model = Perfume
    success_url = '/perfumes/'
    success_message = "The Perfume Review has been deleted!"

    def test_func(self):
        return self.request.user == self.get_object().user

    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, self.success_message)
        return super(PostDelete, self).delete(request, *args, **kwargs)


class EditPerfume(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    '''
    View to edit a perfume review
    '''
    template_name = 'perfume_review/edit_perfume.html'
    model = Perfume
    form_class = PerfumeForm
    success_url = '/perfumes/'
    success_message = 'Perfume Review has been successfully edited!'
    
    def test_func(self):
        return self.request.user == self.get_object().user
