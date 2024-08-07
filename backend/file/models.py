from django.db import models
from authentication.models import User


class File(models.Model):
    file_id = models.AutoField(primary_key=True)
    file = models.FileField(upload_to='%Y/%m/%d/', max_length=5000, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='file_created_by')
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='file_updated_by')

    class Meta:
        db_table = 'files'
        verbose_name = 'File'
        verbose_name_plural = 'Files'
        indexes = [
            models.Index(fields=['file'], name='file_idx'),
        ]
        default_permissions = ['view', 'add', 'change', 'delete']