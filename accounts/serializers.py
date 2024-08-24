from rest_framework.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from rest_framework.serializers import ModelSerializer, CharField, HyperlinkedRelatedField, JSONField
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer, UserSerializer as BaseUserSerializer
from django.utils.translation import gettext_lazy as _
from rest_framework.serializers import Serializer

from accounts.models import Users, PublicNotifications, MobileVerify
from images.models import Image
from storefront_api_generic.kavenegar_config import send_sms


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
        fields = ['mobile_phone', 'password', 'confirm_password']
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
        get_code = MobileVerify.objects.get(mobile_phone=validated_data['mobile_phone'])
        send_sms(get_code.code, get_code.mobile_phone)
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


class VerifyAccountSerializer(Serializer):
    code = CharField(required=True)

    def validate_code(self, data):
        get_code = MobileVerify.objects.get(code=data['code'])
        if get_code:
            get_user = Users.objects.get(mobile_phone=get_code.mobile_phone)
            get_user.is_active = True
            get_user.save()
            get_code.delete()
        else:
            raise ValidationError({'code': _('Invalid code')})
