from django.shortcuts import render
from django.http import HttpResponse

def qna(request):
    return HttpResponse("QnA Page")

def qnadetails(request, pk):
    return HttpResponse(f"QnA Details Page: {pk}")