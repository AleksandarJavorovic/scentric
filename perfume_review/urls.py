from django.urls import path
from .views import AddReview, Perfumes, PerfumeDetail


urlpatterns = [
    path("add_review/", AddReview.as_view(), name="add_review"),
    path("perfumes/", Perfumes.as_view(), name="perfumes"),
    path("<slug:pk>/", PerfumeDetail.as_view(), name="perfume_detail"),
]