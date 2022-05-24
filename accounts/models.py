from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models
from django_extensions.db.models import TimeStampedModel
from .managers import MyUserManager


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=125)
    last_name = models.CharField(max_length=125)
    user_name = models.CharField(max_length=125, unique=True)
    email = models.EmailField()
    phone_number = models.CharField(
        max_length=11,
        validators=[RegexValidator(r"^09[0|1|2|9][0-9]{8}$")],
    )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = "user_name"
    REQUIRED_FIELDS = ["first_name", "last_name", "email", "phone_number"]

    objects = MyUserManager()

    def __str__(self):
        return self.user_name

    @property
    def is_staff(self):
        return True


class OtpCode(models.Model):
    phone_number = models.CharField(max_length=11, unique=True)
    code = models.PositiveSmallIntegerField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.phone_number} - {self.code} - {self.created}"


class UserDocument(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='document')
    national_card = models.ImageField(upload_to='')
    identity_card = models.ImageField(upload_to='')
    passport = models.ImageField(upload_to='', blank=True)
    other = models.ImageField(upload_to='', blank=True)




