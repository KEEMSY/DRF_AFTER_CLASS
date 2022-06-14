from rest_framework import serializers

from userapp.models import User


class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["username", "email", "password", "fullname"]
        extra_kwargs = {
            "password": {'write_only': True},
            "email": {
                'required': '이메일을 입력해주세요',
                'invalid': '알맞은 형식의 이메일을 입력하세요',
            }
        }