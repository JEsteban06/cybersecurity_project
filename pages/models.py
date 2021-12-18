from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class SitePassword(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user')
    site = models.TextField(db_column='site')
    password = models.TextField(db_column='password')

    class Meta:
        db_table = 'SitePassword'
