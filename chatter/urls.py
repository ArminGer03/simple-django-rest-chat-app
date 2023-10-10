from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterUser.as_view(), name='register'),
    # path('login/', user_login, name='login'),
    # path('logout/', user_logout, name='logout'),
]