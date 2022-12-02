from django.shortcuts import render

# Create your views here.
from .models import Ad
from .owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView

base = "ads/templates/ads/"


class AdListView(OwnerListView):
    model = Ad


class AdDetailView(OwnerDetailView):
    model = Ad


class AdCreateView(OwnerCreateView):
    model = Ad


class AdUpdateView(OwnerUpdateView):
    model = Ad


class AdDeleteView(OwnerDeleteView):
    model = Ad
