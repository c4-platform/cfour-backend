from django.db import models
from django.core.files.storage import default_storage


# Create your models here.

class File(models.Model):
    file = models.FileField()
    file_name = models.CharField(max_length=400, blank=True, null=True)
    file_url = models.CharField(max_length=400, blank=True, null=True)

    def __str__(self):
        return self.file_name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.file_name = self.file.name
        self.file_url = default_storage.url(self.file.name)
        return super().save(update_fields=['file_name', 'file_url'])
