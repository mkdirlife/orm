from django.shortcuts import render

# 블로그 글에 sample data
blog_data = [
    {
        "id": 1,
        "title": "첫 번째 글",
        "content": "첫 번째 글 내용입니다.",
    },
    {
        "id": 2,
        "title": "두 번째 글",
        "content": "두 번째 글 내용입니다.",
    },
    {
        "id": 3,
        "title": "세 번째 글",
        "content": "세 번째 글 내용입니다.",
    },
    {
        "id": 4,
        "title": "네 번째 글",
        "content": "네 번째 글 내용입니다.",
    },
]

def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def notice(request):
    return render(request, "notice.html")

def notice1(request, pk):
    print(pk)
    print(blog_data[pk])
    return render(request, "notice1.html")

def contact(request):
    return render(request, "contact.html")

def abcd(request):
    return render(request, "abcd.html")

def hojun(request, s):
    print(s)
    return render(request, "hojun.html")