from django.urls import path
from ariesdh import views

urlpatterns = [
    path('see', views.todolist,name='todolist'),
    path('wkp', views.wkp,name='wkp'),
    path('ssp', views.ssp,name='ssp'),
    
]
