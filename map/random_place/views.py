from django.shortcuts import render

from django.http import HttpResponse
from . import utils


def index(request):
    coord = utils.Coordinate()
    result = coord.coordinate_link
    print(result)
    return HttpResponse(f"<a href={result}> place </a>")