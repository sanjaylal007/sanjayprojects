from . import views
from django.urls import path


urlpatterns = [

    path('register',views.sign,name='sign'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    ]
