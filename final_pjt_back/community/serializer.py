from rest_framework import serializers
from .models import Post, Comment, Reply
class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','title','content')



class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','title','content')



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('post', 'content', 'created_at')


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ('post', 'comment', 'content', 'created_at')
        