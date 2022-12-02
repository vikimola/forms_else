from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView

from .forms import LoginForm
from .models import Article
from .owner import OwnerListView, OwnerCreateView, OwnerDetailView, OwnerUpdateView, OwnerDeleteView

base = "myarts/templates/myarts/"


def home(request):
    return render(request, base + "home.html")


# Errors raised by the form (but not attached to a field)
# are stored in non_field_errors
def log_in(request):
    form = LoginForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.login(request)
        if user:
            login(request, user)
            return redirect(reverse("home"))
    return render(request, base + "logi.html", {"forms": form})


class ArticeListView(LoginRequiredMixin, OwnerListView):
    model = Article
    template_name = base + "article_list.html"


class ArticleDetailView(LoginRequiredMixin, OwnerDetailView):
    model = Article
    template_name = base + "article_detail.html"


class ArticleCreateView(LoginRequiredMixin, OwnerCreateView):
    model = Article
    template_name = base + "article_create_form.html"
    fields = ["title", "text"]
    success_url = reverse_lazy("home")


class ArticleUpdateView(LoginRequiredMixin, OwnerUpdateView):
    model = Article
    template_name = base + "article_update_form.html"
    fields = ["title", "text"]
    success_url = reverse_lazy("view")


class ArticleDeleteView(LoginRequiredMixin, OwnerDeleteView):
    model = Article
    template_name = base + "article_confirm_delete.html"
    success_url = reverse_lazy("view")