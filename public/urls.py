from django.urls import path

from public.views import index


app_name = "public"

urlpatterns = [
    path("", index, name="index"),
]
