from django.urls import path, re_path
from . import views


app_name = "www"

urlpatterns = [
    path("", views.index, name="index"),
    path("articles", views.articles, name="articles"),
    path("documentation", views.documentation, name="documentation"),
    re_path(
        r"^documentation/(?P<name>[\w/]+)$", views.documentation, name="documentation",
    ),
]
