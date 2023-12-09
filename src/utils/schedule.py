from celery import Celery
from datetime import datetime, timedelta

app = Celery('tasks', broker='redis://localhost:6379/0')


@app.task
def my_task():
    print("Task executed at:", datetime.now())


@app.task
def schedule_task():
    eta_time = datetime.now() + timedelta(seconds=5)
    my_task.apply_async(eta=eta_time)


schedule_task()
