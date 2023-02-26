from . import views
from django.urls import path
from django.contrib import admin


admin.site.site_header = "Admin Pannel"
admin.site.site_title = "Welcome"

urlpatterns = [ 
    path('', views.home, name='home'),
    path('authlogin', views.authlogin , name='authlogin'),
    path('authregister', views.authregister , name='authregister'),
    path('authlogout', views.authlogout , name='authlogout')
]