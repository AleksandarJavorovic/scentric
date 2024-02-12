from django.views.generic import ListView
from perfume_review.models import Perfume

# Create your views here.

class Index(ListView):
    template_name = 'blog/index.html'
    model = Perfume
    context_object_name = 'perfumes'

    def get_queryset(self):
        return self.model.objects.all()[:1]