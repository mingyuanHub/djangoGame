from django.shortcuts import render
from django.http import HttpResponse

from hello.models import User


# Create your views here.
def index(request):
    return HttpResponse("123123")

def test(request):
    return HttpResponse("test 2222")