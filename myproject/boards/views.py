# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    # return HttpResponse('Hello, World!')
    return render(request, 'index.html')
