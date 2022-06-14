from rest_framework import serializers

from blog.serializers import ArticleSerializer
from userapp.models import User, UserProfile, Interest


class InterestSerializer(serializers.ModelSerializer):
    same_interest_users = serializers.SerializerMethodField()

    def get_same_interest_users(self, obj):
        user_list = []
        for user_profile in obj.userprofile_set.all():
            user_list.append(user_profile.user.username)

    class Meta:
        model = Interest
        fields = ["name", "same_interest_users"]


class UserProfileSerializer(serializers.ModelSerializer):
    interest = InterestSerializer(many=True)

    class Meta:
        model = UserProfile
        fields = ["interest", "bio", "birthday", "age"]


class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer()
    articles = ArticleSerializer(many=True, source="article_set")

    class Meta:
        model = User
        fields = ["username", "email", "password", "fullname", "userprofile", "articles"]
        extra_kwargs = {
            "password": {'write_only': True},
            "email": {
                "error_messages": {
                    'required': '이메일을 입력해주세요',
                    'invalid': '알맞은 형식의 이메일을 입력하세요',
                }
            }
        }
