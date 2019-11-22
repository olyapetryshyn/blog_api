from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import generics, status, request
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .models import Post
from .serializers import (
    UserSerializer,
    PostDetailSerializer,
    PostCreateListSerializer
)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    # def get_queryset(self, *args):
    #     serializer = UserSerializer(self.queryset, many=True)
    #     return Response(serializer.data)


@method_decorator(login_required, name='dispatch')
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class PostCreateList(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('-date_posted')
    serializer_class = PostCreateListSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    # def get_queryset(self):
    #     user = self.request.user
    #     if user.is_authenticated:
    #         return self.queryset.filter(user=user)
