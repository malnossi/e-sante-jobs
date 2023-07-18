from django.contrib.auth.models import AbstractUser
from django.db import models

from core.models.AbstractIdBase import AbstractIdBase

from .managers import AccountManager


class AccountUser(AbstractUser, AbstractIdBase):
    username = None
    last_name = None
    first_name = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = AccountManager()

    def __str__(self) -> str:
        return self.email

    class Meta:
        db_table = 'users'
        verbose_name = 'user'
        verbose_name_plural = 'users'


class Studentprofile(AbstractIdBase):
    PROMOTIONS = (
        ("FIE1", "Première année de cycle préparatoire"),
        ("FIE2", "Deuxième année de cycle préparatoire"),
        ("FIE3", "Troisième année de cycle ingénieur"),
        ("FIE4", "Quatrième année de cycle ingénieur"),
        ("FIE5", "Cinquième année de cycle ingénieur"),
        ("FIA3", "Troisième année de cycle ingénieur par apprentissage"),
        ("FIA4", "Quatrième année de cycle ingénieur par apprentissage"),
        ("FIA5", "Cinquième année de cycle ingénieur par apprentissage"),
    )
    owner = models.OneToOneField(
        AccountUser, on_delete=models.CASCADE, related_name="student_profile"
    )
    promotion = models.CharField(
        max_length=20, choices=PROMOTIONS, default="FIE1")
    full_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    adress = models.ForeignKey("Adress", on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.full_name
    
    class Meta:
        db_table = 'studentprofils'
        verbose_name = 'studentprofil'
        verbose_name_plural = 'studentprofils'


class Adress(AbstractIdBase):
    street = models.CharField(max_length=200)
    anexxe = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=20)

    @property
    def full_adress(self) -> str:
        return f"{self.street}, {self.anexxe}, {self.city} {self.zip_code}"

    def __str__(self) -> str:
        return self.full_adress
    
    class Meta:
        db_table = 'adresses'
        verbose_name = 'adress'
        verbose_name_plural = 'adresses'