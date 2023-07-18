import uuid

from django.db import models


class AbstractIdBase(models.Model):
    id = models.UUIDField(default=uuid.uuid4(),
                          primary_key=True, unique=True, editable=False)
    
    class Meta:
        abstract = True
