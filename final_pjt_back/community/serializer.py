from rest_framework import serializers
from .models import Article,Comment,reply


class ArticleListSerializer(serializers.ModelSerializer):
    #
    class Meta:
        model = Article
        #fields = "__all__"
        fields = ('id', 'title', 'content')
        only_read_fields = ('users', 'like_users')

class CommentSerializer(serializers.ModelSerializer):
    #
    class Meta:
        model = Comment
        fields = "__all__"
        # fields = ('원하는 필드')

class ArticleDetailSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Article
        fields = "__all__"
        # fields = ('원하는 필드')


class replySerializer(serializers.ModelSerializer):
    #
    class Meta:
        model = reply
        fields = "__all__"
        # fields = ('원하는 필드')

