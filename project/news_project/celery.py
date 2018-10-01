from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_project.settings')

app = Celery(os.environ.get('PROJECT_NAME', 'news_project'))
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))