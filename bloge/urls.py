from django.urls import path
from . import views

urlpatterns = [
    path('',views.bloge_page,name='blkogee_page' )
]