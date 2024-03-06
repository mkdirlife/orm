from django.urls import path
from .views import product, productdetails

urlpatterns = [
    # "product/"URL로 들어오면 product urls.py로 연결하겠다.
    path('', product),                  # 상품 목록
    path("<int:pk>/", productdetails),  # 상품 목록 상세 게시물 
]