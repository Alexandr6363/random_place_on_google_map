from django.shortcuts import render, redirect

from django.http import HttpResponse
from . import utils


def index(request):
    result_list = ""
    for i in range(20):
        coord = utils.Coordinate()
        result = coord.coordinate_link
        result_list += f"<p><a target='_blank' href={result}> place {i} </a>"

    return HttpResponse(result_list)
    # return redirect(result)