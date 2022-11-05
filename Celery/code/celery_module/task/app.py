from celery import Celery, signals

app=Celery("my_module")

def fun(x):
    return x**2

for i in range(0,100):
    app.autodiscover_tasks()
