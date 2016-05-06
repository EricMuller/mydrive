from celery import task
from datetime import datetime


@task()
def add(x, y):
    print(datetime.now())
    return x + y


@task()
def store_file(path):
    print(datetime.now())
    return path
