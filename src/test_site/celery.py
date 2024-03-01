import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_site.settings')

app = Celery('test_site')

app.config_from_object('django.conf:settings', namespace='CELERY')
# app.conf.broker_url = 'redis://redis:6379/0'
# app.conf.result_backend = 'redis://redis:6379/0'

app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
