from . import views
from django.urls import path

urlpatterns=[
    path("home", views.home, name="home"),
    path("log_in", views.log_in, name="log_in"),
    path("view", views.ArticeListView.as_view(), name="view"),
    path("view/<int:pk>", views.ArticleDetailView.as_view(), name="detail"),
    path("create", views.ArticleCreateView.as_view(), name="create"),
    path("view/<int:pk>/update", views.ArticleUpdateView.as_view(), name="update"),
    path("view/<int:pk>/delete", views.ArticleDeleteView.as_view(), name="delete"),

]