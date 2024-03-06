from django.urls import path
from .views import notice, notice_free_board_list, notice_free_board_details, notice_onenone_guide, notice_onenone_details

urlpatterns = [

    # "notice/"URL로 들어오면 notice앱에 urls.py로 연결하겠다.
    path('', notice),                                    # 자유게시판, 1:1게시판 선택 페이지
    path('free/', notice_free_board_list),               # 자유게시판 목록
    path('free/<int:pk>/', notice_free_board_details),   # 자유게시판 상세 게시물
    path('onenone/', notice_onenone_guide),              # 1:1 상담 안내
    path('onenone/<int:pk>/', notice_onenone_details),     # 1:1 상담 상세 게시물
]