from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Perfume


class PerfumeForm(forms.ModelForm):
    """
    Form to add a Perfume Review
    """

    class Meta:
        model = Perfume
        fields = [
            "perfume_brand",
            "concentration",
            "perfume_name",
            "perfume_group",
            "top_notes",
            "middle_notes",
            "base_notes",
            "image",
            "description",
        ]

        description = forms.CharField(widget=RichTextWidget())


        labels = {
            "perfume_brand": "Perfume Brand",
            "concentration": "Concentration",
            "perfume_name": "Perfume Name",
            "perfume_group": "Perfume Group",
            "top_notes": "Top Notes",
            "middle_notes": "Middle Notes",
            "base_notes":"Base Notes",
            "image": "Perfume Image",
            "description": "Perfume Description",
        }