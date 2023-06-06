from django.contrib import admin
from django.urls import path
from . import views
app_name='credentials'
urlpatterns = [
     path('login',views.login,name='login'),
     path('register',views.register,name='register'),
     path('new',views.new,name='new'),
     path('final',views.final,name='final'),
     path('logout',views.logout,name='logout'),

    # path('', views.PersonListView.as_view(), name='person_changelist'),
    # path('add/', views.PersonCreateView.as_view(), name='person_add'),
    # path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
]
