from django.urls import path
from .views import qna, qnadetails

urlpatterns = [
    # "qna/"URL로 들어오면 qna urls.py로 연결하겠다.
    path('', qna),                    # Q&A 목록
    path('<int:pk>/', qnadetails),    # Q&A 상세 게시물
]