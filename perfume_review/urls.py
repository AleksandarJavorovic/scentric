from django.urls import path
from .views import AddReview, Perfumes


urlpatterns = [
    path("add_review/", AddReview.as_view(), name="add_review"),
    path("perfumes/", Perfumes.as_view(), name="perfumes")
]