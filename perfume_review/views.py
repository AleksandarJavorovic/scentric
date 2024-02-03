from django.views.generic import CreateView
from .models import Perfume
from .forms import PerfumeForm

class AddReview(CreateView):
    '''
    Add perfume review
    '''
    template_name = 'add_review.html'
    model = Perfume
    succes_url = '/'
    form_class = PerfumeForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddReview, self).form_valid(form)