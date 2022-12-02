from django import forms
from django.core.validators import MinLengthValidator
from django.forms import ModelForm
from rest_framework import serializers

# from .models import Cars
from .models import Make


# #WORKS
# class CarForm(ModelForm):
#     class Meta:
#         model = Cars
#         fields = "__all__"
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['mileage'] = forms.IntegerField(min_value=0)
#         self.fields["nickname"] = forms.CharField(min_length=2, max_length=255)


class MakeForm(forms.ModelForm):
    class Meta:
        model = Make
        fields = "__all__"
