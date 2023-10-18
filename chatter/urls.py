from django.urls import path

# from rest_framework_nested import routers
from .views import RegisterUser, RoomMessages, UserMenu

# /domain/ <- Domains list
# /domain/{pk}/ <- One domain, from {pk}
# /domain/{domain_pk}/nameservers/ <- Nameservers of domain from {domain_pk}
# /domain/{domain_pk}/nameservers/{pk} <- Specific nameserver from {pk}, of domain from {domain_pk}

# router = routers.SimpleRouter()
# router.register(r'register', RegisterUser, basename='RegisterUser')
#
# domains_router = routers.NestedSimpleRouter(router, r'user', lookup='id')
# domains_router.register(r'messages', RoomMessages, basename='RoomMessages')
#
# urlpatterns = router.urls + domains_router

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
    # path('login/', user_login, name='login'),
    # path('logout/', user_logout, name='logout'),
]