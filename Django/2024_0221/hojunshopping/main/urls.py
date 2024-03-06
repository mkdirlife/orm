from django.urls import path
from .views import index, about, contact

urlpatterns = [

    # ""URL로 들어오면 main앱에 urls.py로 연결하겠다.
    path('', index),              # 잘 나가는 상품 10개 소개
    path('about/', about),        # 회사 소개
    path('contact/', contact),    # 오시는 길
]