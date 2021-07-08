from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class GameUser(models.Model):
    """
    This Class Create Information Model Client Users
    """
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    birthdate = models.CharField(max_length=50)
    about = models.CharField(max_length=140, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "user_profile"
        verbose_name_plural = "User Profile Details"
        ordering = ('-updated_at',)
