from rest_framework import serializers
import re
from .models import AccountUser, Studentprofile, Adress
from .fields import AsymmetricField, AssymetricidField
from django.db import transaction


class AcountUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = AccountUser
        fields = ['email', 'password']

    def validate_password(self, value):
        password_pattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
        if not value:
            raise ValueError("Password not set")
        if not re.match(password_pattern, value):
            raise ValueError("Password must respect rules")
        return value

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        if password is not None:
            user = self.Meta.model(**validated_data)
            user.set_password(password)
            user.save()
            return user


class AdresseSerializer(serializers.ModelSerializer):
    full_adress = serializers.ReadOnlyField()

    class Meta:
        model = Adress
        fields = ['street', 'anexxe', 'city', 'zip_code', 'full_adress']


class StudentProfilSerializer(serializers.ModelSerializer):
    owner = AcountUserSerializer()
    adress = AdresseSerializer()

    class Meta:
        model = Studentprofile
        fields = '__all__'
    
    def create(self, validated_data):
        owner = validated_data.pop('owner', None)
        adress = validated_data.pop('adress', None)
        try:
            with transaction.atomic():
                serializer = AcountUserSerializer(data=owner)
                serializer.is_valid(raise_exception=True)
                owner = serializer.save()
                adress = Adress.objects.create(**adress)
                profil = Studentprofile.objects.create(owner=owner, adress=adress,**validated_data)
                return profil
        except Exception:
            raise ValueError("Something went wrong")
                

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['promotion'] = instance.get_promotion_display()
        return ret

class ResetPasswordDemandeSerializer(serializers.Serializer):
    email = serializers.EmailField()

    class Meta:
        fields = ['email']