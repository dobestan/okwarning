from django.db import models


class HistoryManager(models.Manager):

    def get_domains(self, filter=None):
        queryset = self.get_queryset()
        if filter:
            queryset = queryset.filter(url__contains=filter)

        url_list = queryset.order_by().values_list('url', flat=True).distinct()
        domain_list = ['http://' + url.replace('/', ' ').replace('?', ' ').split()[1] for url in url_list]
        return list(set(domain_list))


class History(models.Model):

    url = models.URLField(
        verbose_name='URL',
    )

    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True, )

    objects = HistoryManager()

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
