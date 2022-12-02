from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name="formok"
base="formok/templates/crispy/"
urlpatterns = [
    path("example", views.example, name="example"),
    path("main", views.main, name="main"),
    path("create", views.Create.as_view(), name="create"),
    path("update", views.Update.as_view(), name="update"),
    path('validate', views.ClassValid.as_view(), name="validate"),
    path("success", views.success, name="success"),
    path("nothing", TemplateView.as_view(template_name=base+"main.html"), name="nothing"),
    path("boring", views.MyView.as_view(template_name=base+"boring.html"), name="boring"),
    path("awesome", views.MyView.as_view(template_name=base+"awesome.html"), name="awesome"),
]
