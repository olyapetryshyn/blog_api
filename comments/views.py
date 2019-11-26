from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import generics, status, request
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly
)
from .models import Comment
from .serializers import (
    CommentChildSerializer,
    CommentDetailSerializer,
    CommentListSerializer
)
from blog.permissions import IsOwnerOrReadOnly
from blog.pagination import PostPageNumberPagination


class CommentCreate(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer
    permission_classes = (IsAuthenticated, )


class CommentDetail(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer
    search_fields = ['content', 'user__first_name']
    permission_classes = (IsAuthenticatedOrReadOnly, )


class CommentList(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = PostPageNumberPagination
