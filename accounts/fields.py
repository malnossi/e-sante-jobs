from django.core.exceptions import ObjectDoesNotExist
from rest_framework.serializers import Field, PrimaryKeyRelatedField
from collections import OrderedDict


class CurrentUserStudentProfileDefault:
    """
    Cette classe est utile pour attaché un
    profil d'autilisateur par defaut aux posts qu'il peut créer
    """

    requires_context = True

    def __call__(self, serializer_field):
        return serializer_field.context["request"].user.student_profile

    def __repr__(self):
        return "%s()" % self.__class__.__name__


class AsymmetricField(Field):
    def __init__(
        self, serializer, many: bool = False, key: str = "id", *args, **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.serializer = serializer
        self.many = many
        self.key = key

    def to_representation(self, value):
        return self.serializer(value, many=self.many).data

    def to_internal_value(self, data):
        if isinstance(data, list):
            ret = [self._get_object(item) for item in data]
        else:
            ret = self._get_object(data)
        return ret

    def _get_object(self, item):
        if item.get(self.key):
            ret = self.serializer.Meta.model.objects.get({self.key: item[self.key]})
        else:
            serializer = self.serializer(data=item)
            serializer.is_valid(raise_exception=True)
            ret = serializer.save()
        return ret


class AssymetricidField(PrimaryKeyRelatedField):
    def __init__(self, serializer, many: bool = False, key:str='id', **kwargs):
        super().__init__(**kwargs)
        self.serializer = serializer
        self.many = many
        self.key=key

    def to_representation(self, value):
        return self.serializer(instance=value, many=self.many).data

    def get_queryset(self):
        if self.queryset:
            return self.queryset
        return self.serializer.Meta.model.objects.all()

    def get_choices(self, cutoff=None):
        queryset = self.get_queryset()
        if queryset is None:
            return {}
        if cutoff is not None:
            queryset = queryset[:cutoff]
        return OrderedDict([
            (
                item.pk,
                self.display_value(item)
            )
            for item in queryset
        ])

    def use_pk_only_optimization(self):
        return False
    
    def to_internal_value(self, data):
        if self.many:
            ret = [self._get_instance(item) for item in data]
        else:
            ret = self._get_instance(data)
        return ret
    def _get_instance(self,item):
        if item.get(self.key):
            instane = self.serializer.Meta.model.objects.get({self.key:item[self.key]})
        else:
            serializer = self.serializer(data=item)
            serializer.is_valid(raise_exception=True)
            instane = serializer.save()
        return instane
