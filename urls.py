from django.urls import path
from . import views



# app_name = 'app_final'

urlpatterns = [
    path('',views.home_page,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('ticketpage/',views.ticket_gen,name='ticket'),
]
