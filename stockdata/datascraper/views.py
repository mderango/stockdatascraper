from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
import matplotlib.pyplot as plt
from io import BytesIO
import base64

from .forms import QueryForm

import matplotlib
matplotlib.use('Agg')


def query(request):
    form = QueryForm()
    return render(request, 'datascraper/form.html', {'form': form})
