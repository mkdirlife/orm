from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def user_signup(request):
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]
        # 선택사항, 입력 안했으면 "" 없는 문자.
        email = request.POST.get("email", "")

        if not (username and password):
            # HttpResponse 실무용도 아님. 실무에서는 page를 띄워줘야 함.
            return HttpResponse("이름과 패스워드는 필수입니다.")

        if User.objects.filter(username=username).exists():
            return HttpResponse("유저이름이 이미 있습니다.")
        if email and User.objects.filter(email=email).exists():
            return HttpResponse("이메일이 이미 있습니다.")

        # create_user 사용해야함. password 암호화 때문 
        user = User.objects.create_user(username, email, password)
        user.save()
        user = authenticate(username=username, password=password)
        # 회원가입 다했으면 바로 로그인 해주는 것.
        login(request, user)
        return redirect("user_profile")
    else:
        # signup.html 은 생html 로 구현해야 함.
        return render(request, "accounts/signup.html")


def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("user_profile")
        else:
            return render(request, "accounts/login.html")
    else:
        return render(request, "accounts/login.html")


def user_logout(request):
    logout(request)
    return redirect("user_login")


@login_required
def user_profile(request):
    return render(request, "accounts/profile.html", {"user": request.user})

