from celery import Celery

app = Celery('tasks', backend='rpc://localhost', broker='pyamqp://guest@localhost//')


@app.task
def add(x, y):
    return x + y
