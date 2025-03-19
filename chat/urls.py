from django.urls import path 
from . import views

urlpatterns = [
    path('',views.chat_interface,name ='chat_interface'),
    path('send_message/',views.send_message,name ='send_message'),
    path('receive_message/',views.receive_message, name ='receive_message'),
]