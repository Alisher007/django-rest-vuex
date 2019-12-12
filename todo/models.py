from django.conf import settings
from django.db import models
# django hosts --> subdomain for reverse
class Todo(models.Model):
    # pk aka id --> numbers
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name