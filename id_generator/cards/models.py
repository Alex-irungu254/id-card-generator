
from django.db import models

import uuid

class IDCard(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    id_number = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/')
    verification_code = models.UUIDField(default=uuid.uuid4, editable=False)
    generated_card = models.ImageField(upload_to='generated/', null=True, blank=True, editable=False)

