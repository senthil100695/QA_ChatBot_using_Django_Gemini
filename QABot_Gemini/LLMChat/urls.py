from django.urls import path
from . import views

from .views import AskGemini

urlpatterns = [
    path('',views.home , name='home'),
    path('chatbot/',AskGemini.as_view(),name='chatbot')
]