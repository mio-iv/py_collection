from django.shortcuts import render
from django.http import HttpResponse    # 追加

# Create your views here.
def index(request):
    html = "<h1>ウエルカムページ</h1>"
    return HttpResponse(html)

def foo(request):
    html = "<h1>foo指定時の挙動（仮）</h1>"
    return HttpResponse(html)

def localStorage(request):
    return render(request, 'index.html')