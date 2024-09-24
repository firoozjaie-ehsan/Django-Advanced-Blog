# from django.shortcuts import render
from django.http import HttpResponse
from .tasks import sendEmail
import requests
from django.core.cache import cache
# Create your views here.e


def send_email(request):
    sendEmail.delay()  # send email task to celery queue
    return HttpResponse("<h1>done sending</h1>")

def test(request):
    if cache.get("test_delay_api") is None:
        response = requests.get("https://1866f1ce-619b-4c2c-bf34-226af19b3e6a.mock.pstmn.io/test/delay/5")
        cache.set("test_delay_api", response.text, timeout=60)  # cache response for 1 minute
    return HttpResponse(cache.get("test_delay_api"))
