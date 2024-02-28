from django.contrib import admin
from django.urls import path
from main.views import (
    index,
    about,
    notice,
    notice1,
    contact,
    abcd,
    hojun,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index),
    path("about/", about),
    path("notice/", notice),
    path("notice/<int:pk>", notice1),
    path("contact/", contact),
    path("a/b/c/d/", abcd),
    path("user/<str:s>", hojun),
]
