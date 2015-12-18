from django.db import models


class HistoryManager(models.Manager):
    pass


class History(models.Model):

    url = models.URLField(
        verbose_name='URL',
    )

    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True, )

    class Meta:
        verbose_name = '검색 기록'
        verbose_name_plural = verbose_name

        ordering = ['-created_at', ]
        get_latest_by = 'created_at'

    def __str__(self):
        return 'Searched "{url}" at {created_at}'.format(
            url=self.url,
            created_at=self.created_at,
        )
