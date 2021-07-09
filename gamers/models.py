from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class GameUser(models.Model):
    """
    This Class Create Information Model Client Users
    """
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    birthdate = models.CharField(max_length=10, blank=True, null=True)
    about = models.CharField(max_length=140, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'gamer_users'
        verbose_name_plural = 'Gamer User Details'
        ordering = ('-updated_at',)

    @property
    def full_name(self) -> str:
        """
        Returns User Full Name
        :return:
        """
        return '{first_name} {last_name}'.format(first_name=self.user.first_name, last_name=self.user.last_name)

    @property
    def username(self) -> str:
        """
        Returns User Name
        :return:
        """
        return self.user.username

    @property
    def email(self) -> str:
        """
        Returns Email Address
        :return:
        """
        return self.user.email

    @property
    def is_active(self) -> str:
        """
        Returns User Status
        :return:
        """
        return 'Active' if self.user.is_active else 'Passive'
