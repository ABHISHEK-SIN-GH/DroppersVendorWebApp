from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index,name='BlogHome'),
   path('home/',views.index,name='BlogHome')
]
