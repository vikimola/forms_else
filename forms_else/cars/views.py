from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
# from .forms import CarForm
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import UpdateView, CreateView, DeleteView

from .forms import MakeForm
from .models import Make, Auto

base = "cars/templates/"


def main(request):
    return render(request, base + "main.html")


def log(request):
    return render(request, base + "registration/login.html")


def log_in(request):
    if request.method == "POST":
        name = request.POST["name"]
        password = request.POST["password"]

        user = authenticate(request, username=name, password=password)

        if user is not None:
            login(request, user)
            # return redirect(reverse("main"))
            return redirect(reverse("cars:main"))
        else:
            messages.add_message(request, messages.INFO, 'Invalid credentials.')
            return redirect(reverse("cars:main"))


class MakeView(LoginRequiredMixin, View):
    def get(self, request):
        ml = Make.objects.all()
        return render(request, base + "make_list.html", {"make_list": ml})


class MakeCreate(LoginRequiredMixin, View):
    template = base + "make_form.html"
    # success_url = base+"make_form.html"
    success_url = reverse_lazy('cars:main')

    def get(self, request):
        form = MakeForm()
        return render(request, self.template, {"form": form})

    def post(self, request):
        form = MakeForm(request.POST)
        if not form.is_valid():
            return render(request, self.template, {"form": form})
        form.save()
        return redirect(self.success_url)


class MakeUpdate(LoginRequiredMixin, View):
    model = Make
    template = base + "make_form.html"
    success_url = reverse_lazy('cars:main')

    def get(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        form = MakeForm(instance=make)
        return render(request, self.template, {"form": form})

    def post(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        form = MakeForm(request.POST, instance=make)
        if not form.is_valid():
            return render(request, self.template, {"form": form})
        form.save()
        return redirect(self.success_url)


class MakeDelete(LoginRequiredMixin, View):
    model = Make
    template = base + "make_confirm_delete.html"
    success_url = reverse_lazy('cars:main')

    def get(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        form = MakeForm(instance=make)
        return render(request, self.template, {"form": form})

    def post(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        make.delete()
        return redirect(reverse("cars:main"))


class CarView(LoginRequiredMixin, View):
    model = Auto
    template = base + "car_list.html"

    def get(self, request):
        car_list = Auto.objects.all()
        make_count = Make.objects.all().count()
        return render(request, self.template, {"auto_list": car_list, "make_count": make_count})


class CarCreate(LoginRequiredMixin, CreateView):
    model = Auto
    fields = "__all__"
    template_name = "cars/templates/auto_form.html"
    success_url = reverse_lazy('cars:main')


class CarUpdate(LoginRequiredMixin, UpdateView):
    model = Auto
    fields = "__all__"
    template_name = "cars/templates/auto_form.html"
    success_url = reverse_lazy('cars:main')


class CarDelete(LoginRequiredMixin, DeleteView):
    model = Auto
    fields = "__all__"
    template_name = "cars/templates/car_confirm_delete.html"
    success_url = reverse_lazy('cars:main')
