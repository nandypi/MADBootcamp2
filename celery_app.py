from celery import Celery
from celery.schedules import crontab

app = Celery('tasks', broker='redis://localhost:6379/0')

app.conf.update(
    timezone='Asia/Kolkata',
    enable_utc=False,
)

@app.task()
def long_running_task():
    import time
    for i in range(10):
        print(f"Processing step {i + 1}/10...")
        time.sleep(1)  # Simulate a long-running task
    return "Task completed!"

from gchat_webhook import main

@app.task()
def greet_gspace_ursers():
    main(msg="Hello from Celery task! This messsage is sheduled for this time....")
    return "Greeting sent to Google Chat space!"


app.conf.beat_schedule = {
    'greet-gspace-users': {
        'task': 'celery_app.greet_gspace_ursers',
        'schedule': crontab(minute=8, hour=17, day_of_month=8)
    }
}