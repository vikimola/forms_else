import html

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from .forms import BasicForm

base = "formok/templates/"


def example(request):
    form = BasicForm()
    return HttpResponse(form.as_table())  # !!!


def main(request):
    return render(request, base + "main.html")


def dumpdata(place, data):
    retval = ""
    if len(data) > 0:
        retval += '<p>Incoming ' + place + ' data:<br/>\n'
        for k, v in data.items():
            retval += html.escape(k) + "=" + html.escape(v) + '</br>\n'
        retval += '</p>\n'
    return retval


class DumpPostView(View):
    def post(self, request):
        dump = dumpdata("POST", request.POST)
        ctx = {'title': 'request.POST', "dump": dump}
        return render(request, base + 'dump.html', ctx)


class Create(DumpPostView):
    def get(self, request):
        form = BasicForm()
        ctx = {"form": form}
        return render(request, base + "form.html", ctx)


class Update(DumpPostView):
    def get(self, request):
        old_data = {
            'title': 'SakaiCar',
            'mileage': 42,
            'purchase_date': '2018-08-14'
        }
        form = BasicForm(old_data)
        ctx = {"form": form}
        return render(request, base + "form.html", ctx)


class ClassValid(DumpPostView):
    def get(self, request):
        old_data = {
            'title': 'SakaiCar',
            'mileage': 42,
            'purchase_date': '2018-08-14'
        }
        form = BasicForm(old_data)
        ctx = {"form": form}
        return render(request, base + "form.html", ctx)

    def post(self, request):
        form = BasicForm(request.POST)
        if not form.is_valid():
            ctx = {"form": form}
            return render(request, base + "form.html", ctx)
        return redirect(reverse("formok:success"))


def success(request):
    return HttpResponse('Yo nice!')


class MyView(View):
    template_name=None
    def get(self, request):
        old_data = {
            'title': 'SakaiCar',
            'mileage': 42,
            'purchase_date': '2018-08-14'
        }
        form = BasicForm(old_data)
        ctx = {"form": form}
        return render(request, self.template_name, ctx)

    def post(self, request):
        form = BasicForm(request.POST)
        if not form.is_valid():
            ctx = {"form": form}
            return render(request, self.template_name, ctx)
        messages.add_message(request, messages.SUCCESS, "Data saved")
        return redirect(reverse("formok:nothing"))
