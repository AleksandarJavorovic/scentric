from django.views.generic import ListView
from perfume_review.models import Perfume
from django.shortcuts import render

# Create your views here.


class Index(ListView):
    '''
    View for the Home Page
    '''
    template_name = "blog/index.html"
    model = Perfume
    context_object_name = "perfumes"

    def get_queryset(self):
        return self.model.objects.all()[:3]

# handling of 404 error
def handling_404(request, exception):
    return render(request, "404.html", {})
