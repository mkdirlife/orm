from django.urls import path
from . import views

# login, logout 이름 사용 X

urlpatterns = [
    # accounts_signup 을 쓰는게 맞는데 user 라고 쓴건 친숙하기 때문
    path("signup/", views.user_signup, name="user_signup"),
    path("login/", views.user_login, name="user_login"),
    path("logout/", views.user_logout, name="user_logout"),
    path("profile/", views.user_profile, name="user_profile"),
]