from django.db import models

from core.models.AbstractIdBase import AbstractIdBase

# Create your models here.


class Post(AbstractIdBase):
    owner = models.ForeignKey(
        "accounts.Studentprofile", on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        db_table = 'posts'
        verbose_name = 'post'
        verbose_name_plural = 'posts'
