from django.urls import path
from . import views

urlpatterns = [
    path("", views.qna_list, name="qna_list"),
    path("<int:pk>/", views.qna_detail, name="qna_detail"),
]