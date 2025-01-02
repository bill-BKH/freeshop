from django.shortcuts import render

# Create your views here.
def profile_page(request):
    return render(request, 'user_panel/user_panel.html')
