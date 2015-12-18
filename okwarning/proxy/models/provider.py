from django.db import models


class ProviderManager(models.Manager):
    pass


class Provider(models.Model):

    objects = ProviderManager()

    name = models.CharField(
        max_length=64,
        unique=True,
        verbose_name='이름',
    )
    homepage = models.URLField(
        unique=True,
        verbose_name='홈페이지',
    )

    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True, )

    class Meta:
        verbose_name = '프록시 서비스 제공자'
        verbose_name_plural = verbose_name
