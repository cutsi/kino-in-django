from . import models 
from django import forms

class ProjekcijaForm(forms.ModelForm):
    class Meta:
        model = models.Projekcija
        fields=['ime_filma','vrijeme_filma','kapacitet_dvorane']

