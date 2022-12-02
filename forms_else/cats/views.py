from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import CatForm
from .models import Breed, Cat

base = "cats/templates/cats/"


class Home(View):

    def get(self, request):
        return render(request, base + "home.html")


class BreedView(ListView):
    model = Breed


class BreedCreate(CreateView):
    # model_name + '_form' suffix in template
    model = Breed
    fields = "__all__"
    success_url = reverse_lazy('bview')  # !!!!!!!!!
    # return HttpResponseRedirect(self.get_success_url()


class BreedUpdate(UpdateView):
    model = Breed
    fields = "__all__"
    success_url = reverse_lazy('bview')
    template_name = base + "breed_update.html"  # to change the default model_name + '_form'


class BreedDelete(DeleteView):
    # A view that displays a confirmation page and deletes an existing object
    model = Breed
    fields = "__all__"
    success_url = reverse_lazy("bview")
    template_name= base+"cat_confirm_delete.html"
    # defeult template name: model_name+'_confirm_delete' at app_name/template_name
