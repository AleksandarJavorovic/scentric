from django.urls import path
from .views import AddReview


urlpatterns = [
    path("add_review/", AddReview.as_view(), name="add_review"),
]