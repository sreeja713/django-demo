from django.db import models
from datetime import datetime
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    created_date = models.DateTimeField(default=datetime.now)
    modified_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name
