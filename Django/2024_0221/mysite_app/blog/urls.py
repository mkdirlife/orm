from django.urls import path
from .views import blog, blogdetails

urlpatterns = [
    path("", blog, name="blog"),
    path("<int:pk>/", blogdetails, name="blogdetails"),
]