from django.shortcuts import render,redirect
from django.http import HttpResponse
def tradexa(request):
    return HttpResponse("<a href=/User/><button>user</button></a><br><br><a href=/Products/><button>products</button></a>")