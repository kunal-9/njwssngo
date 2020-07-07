from django.urls import path
from . import views

urlpatterns = [
    
    

    path('contacts',views.contacts,name = 'contacts'),
    path('donate',views.donate,name = 'donate'),

    path('',views.home,name = 'home'),
    
    
    

]