from rest_framework import serializers
from .models import User, Profile
from heritage.models import Heritage
from heritage.serializers import HeritageDetailSerializer
from review.serializers import ReviewListSerializer
from django.contrib.auth import authenticate


# 회원가입

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'nickname', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['email'], validated_data['nickname'], validated_data['password']
        )
        return user


# 접속중인 유저인지 확인
class UserSerializer(serializers.ModelSerializer):
    survey = serializers.BooleanField()
    email = serializers.EmailField()
    nickname = serializers.CharField()
    like_heritages = HeritageDetailSerializer(many=True, read_only=True)
    dibs_heritages = HeritageDetailSerializer(many=True, read_only=True)
    user_review = ReviewListSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('id', 'email', 'nickname', 'like_heritages', 'dibs_heritages', 'user_review', 'survey')


# 로그인
class LoginUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    class Meta:
        model = User
        fields = ('email', 'password')

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Unable to login with provided credentials.")


# 프로필
class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = ('__all__')


# 비밀번호 확인
class UserPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'password')