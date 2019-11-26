from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Comment


class CommentListSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'content', 'timestamp']


class CommentChildSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'content', 'timestamp']
        read_only_fields = ['user', 'timestamp']


class CommentDetailSerializer(ModelSerializer):
    replies = SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'user', 'content', 'timestamp', 'replies']
        read_only_fields = ['user', 'timestamp']

    @staticmethod
    def get_replies(obj):
        if obj.is_parent:
            return CommentChildSerializer(obj.children(), many=True).data
        return None
