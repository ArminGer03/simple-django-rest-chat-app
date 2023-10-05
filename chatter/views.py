from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer


@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data)
        return Response('ok')
        # serializer.save()
        # return Response(serializer.data, status=status.HTTP_201_CREATED)

# @api_view()
# def register_user(request):
#     return Response('Hello!!!')