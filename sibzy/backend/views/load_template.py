from django.shortcuts import render


def load_template(request, template_path):
    return render(request, template_path + '.html')
