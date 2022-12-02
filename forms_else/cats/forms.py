from django import forms

from .models import Cat


class CatForm(forms.ModelForm):
    def Meta(self):
        model = Cat
        fields = "__all__"

