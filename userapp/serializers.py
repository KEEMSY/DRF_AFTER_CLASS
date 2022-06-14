from rest_framework import serializers

from userapp.models import User, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ["username", "email", "password", "fullname", "userprofile"]
        extra_kwargs = {
            "password": {'write_only': True},
            "email": {
                "error_messages": {
                    'required': '이메일을 입력해주세요',
                    'invalid': '알맞은 형식의 이메일을 입력하세요',
                }

            }
        }
