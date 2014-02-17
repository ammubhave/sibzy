from django.shortcuts import render
from django.conf import settings
from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def load_template(request, template_path):
    ''' Render the static template <template_path>.html

    **Arguments:**
        *template_path*: The template filename without the extension

    **Returns:**
        The contents of the file <template_path.html> rendered
    '''

    if not request.user.is_staff and settings.ON_SERVER:
        return render(request, 'SibzyLanding/sibzy_template.htm')
    return render(request, template_path + '.html')
