from rest_framework import serializers
from .models import Movie, Comment, Genre, MovieGenres, CustomRecommend


class MovieListSerializer(serializers.ModelSerializer):
    #
    class Meta:
        model = Movie
        fields = "__all__"


class commentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        # read_only_fields는 읽기 전용 -> 업데이트 프로세스 포함시키지 않는 필드
        read_only_fields = ('movie_id', 'user_id')


class genreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class movieGenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieGenres
        fields = '__all__'


class CustomRecommendSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomRecommend
        fields = '__all__'

