# from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.views.decorators.cache import cache_page
from .tasks import sendEmail

# Create your views here.e


def send_email(request):
    sendEmail.delay()  # send email task to celery queue
    return HttpResponse("<h1>done sending</h1>")


@cache_page(60)
def test(request):
    response = requests.get(
        "https://1866f1ce-619b-4c2c-bf34-226af19b3e6a.mock.pstmn.io/test/delay/5"
    )
    return HttpResponse(response)
