from django.shortcuts import render
from django.views.decorators.http import require_http_methods


@require_http_methods(['GET',])
def home_view(request):
    # Just render a simple page for GET
    return render(request, 'service/home.html')