from django.views.generic import CreateView
from .models import Perfume


class AddReview(CreateView):
    '''
    Add perfume review
    '''
    template_name = 'perfume_review/add_review.html'
    model = Perfume
    succes_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(addReview, self).form_valid(form)