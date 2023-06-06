from django.contrib import admin
from django.urls import path, include
from . import views
app_name='bank'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    ]
