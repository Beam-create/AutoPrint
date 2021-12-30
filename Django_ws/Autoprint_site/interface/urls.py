from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='AutoPrint-home'),
    path('interaction/', views.interaction, name='interaction'),
    path('buttons/', views.buttons, name='buttons'),
    path('printer_status', views.Printer_status, name='Printer_status')
]
