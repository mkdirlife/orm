from django.urls import path
from .views import index, about, contact

urlpatterns = [
    # tutorialdjango urls.py 에 ""URL로 들어오면 main앱에 urls.py로 들어온것임.
    path('', index),
    path('about/', about),
    path('contact/', contact),
]