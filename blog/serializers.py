from django.contrib.auth.models import User
from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField
)
from .models import Post
from comments.serializers import CommentListSerializer
from comments.models import Comment


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class PostDetailSerializer(ModelSerializer):
    user = SerializerMethodField()
    comments = SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['user']

    @staticmethod
    def get_user(obj):
        return str(obj.user.username)

    @staticmethod
    def get_comments(obj):
        content_type = obj.get_content_type
        object_id = obj.id
        c_qs = Comment.objects.filter_by_instance(obj)
        comments = CommentListSerializer(c_qs, many=True).data
        return comments


class PostCreateListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(view_name='post-detail')

    class Meta:
        model = Post
        fields = ['url', 'id', 'title', 'content', 'date_posted', 'user']
        read_only_fields = ['id', 'date_posted', 'user']
