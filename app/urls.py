from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('signup',views.signup, name='signup'),
    path('signin',views.signin, name='signin'),
    path('signout',views.signout, name='signout'),
    path('profile',views.profile, name='profile'),
    path('blog',views.blog, name='blog'),
    path('details/<str:slug>',views.details, name='details')

    
]
