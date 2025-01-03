from django.shortcuts import render

# Create your views here.


def bloge_page(request):
    return render(request, 'blog/bloge.html')