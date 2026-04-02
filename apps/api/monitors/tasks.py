# monitors/tasks.py

import requests
from celery import shared_task
from .models import Monitor, Check

@shared_task
def run_checks():
    monitors = Monitor.objects.all()

    for m in monitors:
        try:
            r = requests.get(m.url, timeout=5)
            status = r.status_code == 200
            response_time = r.elapsed.total_seconds()
        except:
            status = False
            response_time = 0

        Check.objects.create(
            monitor=m,
            status=status,
            response_time=response_time
        )