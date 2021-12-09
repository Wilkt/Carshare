from django.urls import path

from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('select',views.select, name='select'),
    path('payment',views.payment, name='payment'),
    path('location',views.location, name='location'),
    path('review',views.review, name='review'),
    path('signupdriver',views.signupdriver, name='signupdriver'),
    path('login',views.login, name='login'),
    path('registration',views.registration, name='registration'),
    path('logdriver',views.logdriver, name='logdriver')
]