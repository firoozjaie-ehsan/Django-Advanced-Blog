# from django.shortcuts import render
from django.http import HttpResponse
from .tasks import sendEmail

# Create your views here.e


def send_email(request):
    sendEmail.delay()  # send email task to celery queue
    return HttpResponse("<h1>done sending</h1>")
