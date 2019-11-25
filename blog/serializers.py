from django.contrib.auth.models import User
from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField
)
from .models import Post


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class PostDetailSerializer(ModelSerializer):
    user = SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['user']

    @staticmethod
    def get_user(obj):
        return str(obj.user.username)


class PostCreateListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(view_name='post-detail')

    class Meta:
        model = Post
        fields = ['url', 'id', 'title', 'content', 'date_posted', 'user']
        read_only_fields = ['id', 'date_posted', 'user']
