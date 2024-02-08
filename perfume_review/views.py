from django.views.generic import CreateView, ListView, DetailView
from .models import Perfume
from .forms import PerfumeForm


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
    success_url = '/'
    form_class = PerfumeForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddReview, self).form_valid(form)