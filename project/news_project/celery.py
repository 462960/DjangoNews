from celery import Celery
import os

app = Celery(os.environ.get('PROJECT_NAME', 'news_project'))
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
