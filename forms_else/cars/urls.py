from django.urls import path

from . import views

app_name = "cars"
urlpatterns = [
    path("main", views.main, name="main"),
    path("log", views.log, name="log"),
    path("log_in", views.log_in, name="log_in"),
    path("lookup", views.MakeView.as_view(), name="lookup"),
    path("lookup/create", views.MakeCreate.as_view(), name="mcreate"),
    path("lookup/<int:pk>/update", views.MakeUpdate.as_view(), name="mupdate"),
    path("lookup/<int:pk>/delete", views.MakeDelete.as_view(), name="mdelete"),
    path("cars", views.CarView.as_view(), name="cars"),
    path("cars/create", views.CarCreate.as_view(), name="ccreate"),
    path("cars/<int:pk>/update", views.CarUpdate.as_view(), name="cupdate"),
    path("cars/<int:pk>/delete", views.CarDelete.as_view(), name="cdelete"),
    # path("update", views.Update.as_view(), name="update"),

]
