from celery import Task

from proxy.models import Provider


class SpeedTestTask(Task):

    def run(self, *args, **kwargs):

        for provider in Provider.objects.all().order_by('?'):
            provider.run_speed_test()
