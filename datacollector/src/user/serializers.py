from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password


def hash_pass(value):
    return make_password(value)


class TeacherSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Teacher
        fields = '__all__'


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value


class TeacherRegisterSerializer(serializers.ModelSerializer):
    kbtu_mail = serializers.EmailField(style={'placeholder': 'KBTU email'})
    password = serializers.CharField(write_only=True, style={'input_type': 'password', 'placeholder': 'Password'})
    confirm_password = serializers.CharField(write_only=True, style={'input_type': 'password',
                                                                     'placeholder': 'Confirm password'})

    class Meta:
        model = Teacher
        fields = ('id', 'kbtu_mail', 'password', 'confirm_password')

    def create(self, validated_data):
        user = Teacher.objects.create_user(**validated_data)
        return user

    def validate_kbtu_mail(self, data):
        # if "@kbtu.kz" not in data:
        #     raise serializers.ValidationError("You must register email with @kbtu.kz domain.")
        return data

    def validate(self, data):
        if not data['password'] or not data['confirm_password']:
            raise serializers.ValidationError("Please enter a password and confirm it.")

        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Those passwords don't match")

        # data['password'] = hash_pass(data['password'])
        # data.pop('confirm_password', None)
        # return super().validate(data)
        return data

    # def validate_password(self, value: str) -> str:
    #     """
    #     Hash value passed by user.
    #
    #     :param value: password of a user
    #     :return: a hashed version of the password
    #     """
    #     return make_password(value)


class ProfileFullSerializer(serializers.ModelSerializer):
    user = TeacherSerializer(read_only=True)
    faculty = serializers.ChoiceField(Profile.FACULTIES)
    degree = serializers.ChoiceField(Profile.DEGREES)
    gender = serializers.ChoiceField(Profile.GENDER)
    avatar_url = serializers.SerializerMethodField('get_avatar_url')

    def get_avatar_url(self, obj):
        return 'http://localhost:8000' + obj.avatar.url

    class Meta:
        model = Profile
        fields = '__all__'


class ProfileShortSerializer(serializers.ModelSerializer):
    user = TeacherSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ('kbtu_mail', 'is_active', 'full_name', 'phone', 'faculty', 'degree', 'gender', 'avatar')
