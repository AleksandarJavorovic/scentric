from django.urls import path
from .views import (
    AddReview, Perfumes, PerfumeDetail,
    DeletePerfume, EditPerfume
)


urlpatterns = [
    path("add_review/", AddReview.as_view(), name="add_review"),
    path("perfumes/", Perfumes.as_view(), name="perfumes"),
    path("<slug:pk>/", PerfumeDetail.as_view(), name="perfume_detail"),
    path("delete/<slug:pk>/", DeletePerfume.as_view(), name="delete_perfume"),
    path("edit/<slug:pk>/", EditPerfume.as_view(), name="edit_perfume"),
]
