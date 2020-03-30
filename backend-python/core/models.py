from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.username = username
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', True)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser=True')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisa ter is_staff=True')

        return self._create_user(username, email, password, **extra_fields)

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)


class ControlLogin(AbstractUser):
    id_ong = models.AutoField(primary_key=True, auto_created=True)
    username = models.CharField('Usuário', max_length=50, unique=True)
    photo = models.ImageField('Foto', upload_to='photo_profile/', null=True, blank=True)
    email = models.EmailField('Email')
    city = models.CharField('Cidade', max_length=255)
    uf = models.CharField('Estado', max_length=2)
    phone_number = models.CharField('Whatsapp', max_length=11)
    is_staff = models.BooleanField('Membro da equipe', default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'password', 'email', 'phone_number', 'city', 'uf']

    objects = UserManager()

    class Meta:
        db_table = 'ong_login'
        managed = True

    def __str__(self):
        return str(self.username)


class Incidents(models.Model):
    id_incidents = models.AutoField(primary_key=True)
    title_incident = models.CharField('Caso', max_length=100)
    description_incident = models.TextField('Descrição')
    value_incident = models.DecimalField('Valor em Reais', max_digits=8, decimal_places=2)
    ong_id = models.ForeignKey(ControlLogin, on_delete=models.PROTECT)

    class Meta:
        db_table = 'ong_incident'
        managed = True

    def __str__(self):
        return str(self.title_incident)
