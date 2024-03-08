from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name='index'),    
    path("about/", views.about, name='about'),
    path("contact/", views.contact, name='contact'),                  
]
# name 이 있는 이유는 이 URL의 고유 별칭입니다.
# 템플릿 같은 곳에서 이 별칭을 이용해 이 URL에 접근할 수 있습니다.