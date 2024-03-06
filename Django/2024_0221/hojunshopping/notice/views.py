from django.shortcuts import render
from django.http import HttpResponse

def notice(request):
    return HttpResponse("Free Board, One and One Select")

def notice_free_board_list(request):
    return HttpResponse("Free Board list")

def notice_free_board_details(request, pk):
    return HttpResponse(f"Free Board Details Page: {pk}")

def notice_onenone_guide(request):
    return HttpResponse("One and One Guide")

def notice_onenone_details(request, pk):
    return HttpResponse(f"One and One Details Page: {pk}")