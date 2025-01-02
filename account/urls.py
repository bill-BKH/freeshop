from django.urls import path
from . import views

urlpatterns = [
    path('',views.login_page,name='account_page'),
    path('',views.register_page,name='register_page'),
]