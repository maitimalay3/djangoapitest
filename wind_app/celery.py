import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wind_app.settings")
app = Celery("wind_app")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()