from django.urls import path, include
from .views import RegisterUser, RoomMessages, UserMenu

# 'basename' is optional. Needed only if the same viewset is registered more than once
# Official DRF docs on this option: http://www.django-rest-framework.org/api-guide/routers/

# messages_detail = RoomMessages.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })

messages_list = RoomMessages.as_view({
    'get': 'list',
    'post': 'create'
})

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('user/<id>/', UserMenu.as_view(), name='user_menu'),
    path('user/<id>/room/<room_pk>/', messages_list, name='room_messages'),
]