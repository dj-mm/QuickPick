from django.urls import path
from. import views



urlpatterns = [
    path('index/',views.index),
    path('about/',views.about),
    path('contact/',views.contact),
    path('about/',views.about),
    path('signin/',views.signin),
    path('signup/',views.signup),
    path('product/',views.product),
    
    
    
    
]
