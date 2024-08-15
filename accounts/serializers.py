from rest_framework.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from rest_framework.serializers import ModelSerializer, CharField, HyperlinkedRelatedField
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer, UserSerializer as BaseUserSerializer
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now, timedelta

from accounts.models import Users, PublicNotifications, EmailVerify
from images.models import Image
from storefront_api_generic.generate_random_code import random_code
from storefront_api_generic.send_email import send_email


class UserCreateSerializer(BaseUserCreateSerializer):
    confirm_password = CharField(write_only=True, required=True, style={'input_type': 'password'},
                                 help_text=_(
                                 "password must be 8 character.\n"
                                 "The password must not be the same as the username and email.\n"
                                 "The password must be a combination of words and letters.\n"
                                 "Password must have at least one uppercase character."
                                 ))

    class Meta(BaseUserCreateSerializer.Meta):
        model = Users
        fields = ['email', 'username', 'password', 'confirm_password']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True},
        }

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise ValidationError('Passwords must be match')
        try:
            validate_password(data['password'])
        except ValidationError as e:
            raise ValidationError({'password': e})
        return data

    def create(self, validated_data):
        del validated_data['confirm_password']
        user = Users.objects.create_user(**validated_data)
        user.is_active = False
        user.save()

        email_verify = EmailVerify.objects.create(
            email=validated_data['email'],
            code=random_code(),
            expired_code=now() + timedelta(minutes=2),
        )
        # send_email(email_verify, email_verify.code)
        return user


class UserSerialize(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        model = Users
        fields = ['username', 'email', 'mobile_phone', 'first_name', 'last_name', 'sheba_number', 'bio',
                  'date_joined', 'gender', 'image']


class PublicNotificationSerializer(ModelSerializer):
    image = HyperlinkedRelatedField(
        view_name='image:details_image',
        queryset=Image.objects.all()
    )

    class Meta:
        model = PublicNotifications
        fields = ['create_at', 'title', 'description', 'image', 'url', 'is_read']


class ReadPublicNotificationSerializer(ModelSerializer):
    class Meta:
        model = PublicNotifications
        fields = ['is_read']
