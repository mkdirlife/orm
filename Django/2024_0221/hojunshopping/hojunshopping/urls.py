from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", include("main.urls")),
    # ""URL로 들어오면 main앱에 urls.py로 연결하겠다.
    # path('', index),              => 잘 나가는 상품 10개 소개
    # path('about/', about),        => 회사 소개
    # path('contact/', contact),    => 오시는 길

    path("product/", include("product.urls")),
    # "product/"URL로 들어오면 product urls.py로 연결하겠다.
    # path('product/', product), => 상품 목록
    # path("product/<int:pk>/", productdetails), => 상품 목록 상세 게시물 
    
    path("qna/", include("qna.urls")),
    # "qna/"URL로 들어오면 qna urls.py로 연결하겠다.
    # path('qna/', qna),                    => Q&A 목록
    # path('qna/<int:pk>/', qnadetails),    => Q&A 상세 게시물


    path("notice/", include("notice.urls")),
    # "notice/"URL로 들어오면 notice앱에 urls.py로 연결하겠다.
    # path('notice/', notice'),  # 자유게시판, 1:1게시판 선택 페이지
    # path('notice/free/', notice_free_board_list),  # 자유게시판 목록
    # path('notice/free/<int:pk>/', notice_free_board_details),  # 자유게시판 상세 게시물
    # path('notice/onenone/', notice_onenone_guide),  # 1:1 상담 안내
    # path('notice/onenone/<int:pk>/', notice_onenone_details),  # 1:1 상담 상세 게시물
]