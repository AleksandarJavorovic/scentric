from django.contrib import admin
from .models import Perfume


@admin.register(Perfume)
class PerfumeAdmin(admin.ModelAdmin):
    list_display = (
        "perfume_brand",
        "perfume_name",
        "perfume_group",
        "top_notes",
        "middle_notes",
        "base_notes",
        "image",
        "description",
        "base_notes",
    )
    list_filter = ("perfume_group",)
