from django.db import models


class SpeedManager(models.Manager):

    def get_queryset(self):
        return super(models.Manager, self).get_queryset().select_related(
            'provider',
        )


class Speed(models.Model):

    provider = models.ForeignKey(
        'Provider',
    )

    elapsed_time = models.FloatField(
        verbose_name='경과 시간',
    )

    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True, )

    objects = SpeedManager()

    class Meta:
        verbose_name = '프록시 서비스 제공자 속도측정'
        verbose_name_plural = verbose_name

        ordering = ['-created_at', ]
        get_latest_by = 'created_at'

    def __str__(self):
        return "Elapsed {elapsed_time} seconds on {provider_name} at {created_at}".format(
            elapsed_time=self.elapsed_time,
            provider_name=self.provider.name,
            created_at=self.created_at,
        )
