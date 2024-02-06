from django.db import models
from django.contrib.auth.models import User

from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField

#Choices

PERFUME_GROUPS = (
    ("amber", "Amber"),
    ("aromatic", "Aromatic"),
    ("chypre", "Chypre"),
    ("citrus", "Citrus"),
    ("floral", "Floral"),
    ("leather", "Leather"),
    ("woody", "Woody"),
)

CONCENTRATIONS = (
    ("eau_fraiche", "Eau Fraiche"),
    ("eau_de_cologne", "Eau de Cologne"),
    ("eau_de_toilette", "Eau de Toilette"),
    ("eau_de_parfum", "Eau de Parfum"),
    ("parfum", "Parfum"),
    ("extrait_de_parfum", "Extrait de Parfum"),
)


# Create your models here.

class Perfume(models.Model):
    '''
    The Model to create perfume review
    '''
    user = models.ForeignKey(
        User, related_name="perfume_reviewer", on_delete=models.CASCADE
    )
    slug = models.SlugField(max_length=200, default="", null=False)
    perfume_brand = models.CharField(max_length=100, null=False, blank=False)
    concentration = models.CharField(max_length=50, choices=CONCENTRATIONS, default="eau_de_toilette")
    perfume_name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    perfume_group = models.CharField(max_length=30, choices=PERFUME_GROUPS, default="woody")
    top_notes = models.CharField(max_length=200, null=False, blank=False)
    middle_notes = models.CharField(max_length=200, null=False, blank=False)
    base_notes = models.CharField(max_length=200, null=False, blank=False)
    image = ResizedImageField(
        size=[400, None],
        quality=75,
        upload_to="perfume_reviwes/",
        force_format="WEBP",
        blank=False,
        null=False,
    )
    description = RichTextField(max_length=1000, null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.perfume_brand} - {self.perfume_name} | written by {self.user}"