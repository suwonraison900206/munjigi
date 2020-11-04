from rest_framework import serializers
from .models import Review


# 리뷰 리스트

class ReviewListSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%Y-%m-%d')
    updated_at = serializers.DateTimeField(format='%Y-%m-%d')
    users = serializers.StringRelatedField(source='user.nickname', read_only=True)
    k_name = serializers.StringRelatedField(source='heritage.k_name', read_only=True)
    imageurl = serializers.StringRelatedField(source='heritage.imageurl', read_only=True)
    class Meta:
        model = Review
        fields = ('id', 'title', 'content', 'created_at', 'updated_at', 'users', 'heritage', 'k_name', 'imageurl')


class ReviewSerializer(serializers.ModelSerializer):
    users = serializers.StringRelatedField(source='user.nickname', read_only=True)
    class Meta:
        model = Review
        fields = ('__all__')
