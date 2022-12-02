from django.urls import path
from . import views
urlpatterns=[
    path("home", views.Home.as_view(), name="home"),
    path("bview", views.BreedView.as_view(), name="bview"),
    path("bcreate", views.BreedCreate.as_view(), name="bcreate"),
    path("<int:pk>/bupdate", views.BreedUpdate.as_view(), name="bupdate"),
    path("<int:pk>/bdelete", views.BreedDelete.as_view(), name="bdelete"),
]