from rest_framework import generics, permissions
from .models import CustomUser
from .serializers import RegisterSerializer, UserSerializer
from .permissions import IsAdmin, IsEditorOrAdmin
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdmin]


@api_view(['GET', 'POST', 'DELETE'])
def content_view(request):
    if request.method == 'GET':
        return Response({"message": "Public content visible to all roles"})

    if request.method == 'POST':
        if request.user.role in ['admin', 'editor']:
            return Response({"message": f"Content created by {request.user.username}"})
        return Response({"error": "Not allowed"}, status=403)

    if request.method == 'DELETE':
        if request.user.role in ['admin', 'editor']:
            return Response({"message": f"Content deleted by {request.user.username}"})
        return Response({"error": "Not allowed"}, status=403)
