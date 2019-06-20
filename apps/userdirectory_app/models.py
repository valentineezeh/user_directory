from django.db import models

# Create your models here.

class UserDirectory(models.Model):
    name = models.CharField(max_length = 45)
    email = models.CharField(max_length = 45)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = models.Manager()
    class Meta:
      db_table = "userdirectory"
