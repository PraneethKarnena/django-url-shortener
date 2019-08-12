from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . import models
from . import serializers
import string
import random


@require_http_methods(['GET',])
def home_view(request):
    # Just render a simple page for GET
    return render(request, 'service/home.html')


@api_view(['POST'])
def url_shortener_view(request):
    # the URL entered by the User
    users_url = request.data['url']

    # Gets the shortened record and serialize it
    service = shorten_url(users_url)
    service_serializer = serializers.ServiceSerializer(service, many=False)
    return Response(data={'success': True, 'data': service_serializer.data}, status=status.HTTP_201_CREATED)


def generate_random_string(string_length=6):
    # Generates a random string
    random_string = ''
    alpha_numerals = string.ascii_letters + string.digits
    for _ in range(string_length):
        random_string = random_string + random.choice(alpha_numerals)
    return random_string


def shorten_url(url):
    # Gets a random string and validates it against the database
    random_string = generate_random_string()
    service, created = models.UrlModel.objects.get_or_create(slug=random_string)
    if created:
        service.url = url
        service.save()
        return service
    else:
        shorten_url(url)
