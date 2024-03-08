from django.shortcuts import render


def qna_list(request):
    return render(request, "qna/qna_list.html")


def qna_detail(request, pk):
    return render(request, "qna/qna_detail.html")