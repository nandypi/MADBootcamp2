from celery import Celery

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