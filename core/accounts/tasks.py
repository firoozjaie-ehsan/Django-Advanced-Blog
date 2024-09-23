from celery import shared_task
from time import sleep


@shared_task
def sendEmail():
    sleep(3)  # Simulate some heavy task
    print("done sending email")
