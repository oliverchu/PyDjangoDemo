# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from  django.http import HttpResponse


# Create your views here.
def hello(request):
    student = {
        'name': 'Oliver Chu',
        'age': '24'
    }
    body = render(request, 'hello.html', {'hello': student})
    # body= 'sadasd'
    return HttpResponse(body)
    # For this commit,I create a new branch.
