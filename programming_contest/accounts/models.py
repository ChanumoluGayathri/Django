from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
#from django.utils.translation import ugettext_lazy as _
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, email, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

class Userdata(models.Model):
    code = models.TextField(max_length=1000)
    input_part = models.TextField(max_length=100)
    output_part = models.TextField(max_length=100)
    score = models.IntegerField(default=0)
    def __str__(self):
        return self.output_part

class EvenOdd(models.Model):
    tnum=models.IntegerField(default=0)
    input=models.CharField(max_length=100)
    output=models.TextField(max_length=100)
    def __str__(self):
         return '{}{}{}'.format(self.tnum, self.input, self.output)

class ReverseNum(models.Model):
    tnum=models.IntegerField(default=0)
    input=models.CharField(max_length=100)
    output=models.TextField(max_length=100)
    def __str__(self):
         return '{}{}{}'.format(self.tnum, self.input, self.output)

class PrimeNum(models.Model):
    tnum=models.IntegerField(default=0)
    input=models.CharField(max_length=100)
    output=models.TextField(max_length=100)
    def __str__(self):
         return '{}{}{}'.format(self.tnum, self.input, self.output)

class PostiveNum(models.Model):
    tnum=models.IntegerField(default=0)
    input=models.CharField(max_length=100)
    output=models.TextField(max_length=100)
    def __str__(self):
         return '{}{}{}'.format(self.tnum, self.input, self.output)

class MagicNum(models.Model):
    tnum=models.IntegerField(default=0)
    input=models.CharField(max_length=100)
    output=models.TextField(max_length=100)
    def __str__(self):
         return '{}{}{}'.format(self.tnum, self.input, self.output)

class CapitalizeVowels(models.Model):
    tnum=models.IntegerField(default=0)
    input=models.CharField(max_length=100)
    output=models.TextField(max_length=100)
    def __str__(self):
         return '{}{}{}'.format(self.tnum, self.input, self.output)

class UnitNum(models.Model):
    tnum=models.IntegerField(default=0)
    input=models.CharField(max_length=100)
    output=models.TextField(max_length=100)
    def __str__(self):
         return '{}{}{}'.format(self.tnum, self.input, self.output)

class Tensdigit(models.Model):
    tnum=models.IntegerField(default=0)
    input=models.CharField(max_length=100)
    output=models.TextField(max_length=100)
    def __str__(self):
         return '{}{}{}'.format(self.tnum, self.input, self.output)

class Palindrome(models.Model):
    tnum=models.IntegerField(default=0)
    input=models.CharField(max_length=100)
    output=models.TextField(max_length=100)
    def __str__(self):
         return '{}{}{}'.format(self.tnum, self.input, self.output)

class Armstrong(models.Model):
    tnum=models.IntegerField(default=0)
    input=models.CharField(max_length=100)
    output=models.TextField(max_length=100)
    def __str__(self):
         return '{}{}{}'.format(self.tnum, self.input, self.output)

class QuestionKey(models.Model):
    key = models.CharField(max_length=50)
    def __str__(self):
        return self.key

class HomeTime(models.Model):
    home=models.TimeField()
    def __str__(self):
        return self.home

class LoginTime(models.Model):
    login=models.TimeField()
    def __str__(self):
        return self.login

class TestTime(models.Model):
    test=models.TimeField()
    def __str__(self):
        return self.test

class FinishTime(models.Model):
    finish=models.TimeField()
    def __str__(self):
        return self.finish

class HiddenEvenOdd(models.Model):
    tnum=models.IntegerField(default=0)
    input=models.CharField(max_length=100)
    output=models.TextField(max_length=100)
    def __str__(self):
         return '{}{}{}'.format(self.tnum, self.input, self.output)

class HiddenReverseNum(models.Model):
    tnum=models.IntegerField(default=0)
    input=models.CharField(max_length=100)
    output=models.TextField(max_length=100)
    def __str__(self):
         return '{}{}{}'.format(self.tnum, self.input, self.output)

class HiddenPrimeNum(models.Model):
    tnum=models.IntegerField(default=0)
    input=models.CharField(max_length=100)
    output=models.TextField(max_length=100)
    def __str__(self):
         return '{}{}{}'.format(self.tnum, self.input, self.output)

class HiddenPositiveNum(models.Model):
    tnum=models.IntegerField(default=0)
    input=models.CharField(max_length=100)
    output=models.TextField(max_length=100)
    def __str__(self):
         return '{}{}{}'.format(self.tnum, self.input, self.output)

class HiddenMagicNum(models.Model):
    tnum=models.IntegerField(default=0)
    input=models.CharField(max_length=100)
    output=models.TextField(max_length=100)
    def __str__(self):
         return '{}{}{}'.format(self.tnum, self.input, self.output)

class HiddenCapitalizeVowels(models.Model):
    tnum=models.IntegerField(default=0)
    input=models.CharField(max_length=100)
    output=models.TextField(max_length=100)
    def __str__(self):
         return '{}{}{}'.format(self.tnum, self.input, self.output)

class HiddenUnitNum(models.Model):
    tnum=models.IntegerField(default=0)
    input=models.CharField(max_length=100)
    output=models.TextField(max_length=100)
    def __str__(self):
         return '{}{}{}'.format(self.tnum, self.input, self.output)

class HiddenTensdigit(models.Model):
    tnum=models.IntegerField(default=0)
    input=models.CharField(max_length=100)
    output=models.TextField(max_length=100)
    def __str__(self):
         return '{}{}{}'.format(self.tnum, self.input, self.output)

class HiddenPalindrome(models.Model):
    tnum=models.IntegerField(default=0)
    input=models.CharField(max_length=100)
    output=models.TextField(max_length=100)
    def __str__(self):
         return '{}{}{}'.format(self.tnum, self.input, self.output)

class HiddenArmstrong(models.Model):
    tnum=models.IntegerField(default=0)
    input=models.CharField(max_length=100)
    output=models.TextField(max_length=100)
    def __str__(self):
         return '{}{}{}'.format(self.tnum, self.input, self.output)

class UserHiddenData(models.Model):
    tnum=models.IntegerField(default=0)
    input=models.CharField(max_length=100)
    output=models.TextField(max_length=100)
    def __str__(self):
         return '{}{}{}'.format(self.tnum, self.input, self.output)
