from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('send/', views.send, name='messages-send'),
    path('inbox/', views.inbox, name='messages-inbox'),
    path('conversation/<int:pk>/', views.conversation, name='messages-conversation'),
    #path('sent/', views.sent, name='messages-sent'),
]