from django.contrib import admin
from django.urls import path
from home.views import web1 
from kontak.views import web2 
from vidio.views import web3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', web1),
    path('kontak', web2),
    path('vidio', web3),
]
