import os, urllib
import re
from django.shortcuts import render, redirect
from django.http import HttpResponse
from sibzy.api.models import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required

@login_required
def user_profile_get(request):
    response = HttpResponseRedirect('/')
    response.set_cookie('a', '')
    response.set_cookie('f', '')
    return response

@login_required
def user_profile_put(request):
    return HttpResponse('')