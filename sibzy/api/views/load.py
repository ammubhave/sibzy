import os
from django.shortcuts import render
from django.http import HttpResponse

"Handles static webpages, served directly from the templates directory"
def load(request, template_path):
    return render(request, template_path + '.html')