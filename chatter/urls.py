from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('user:<id>/', views.UserMenu.as_view(), name='user menu')
    # path('login/', user_login, name='login'),
    # path('logout/', user_logout, name='logout'),
]