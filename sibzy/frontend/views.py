from django.shortcuts import render
import settings

def load_template(request, template_path):
    ''' Render the static template <template_path>.html

    **Arguments:**
        *template_path*: The template filename without the extension

    **Returns:**
        The contents of the file <template_path.html> rendered
    '''
    if not request.user.is_staff or not settings.DEBUG:
        return render(request, 'temp_landing.html')
    return render(request, template_path + '.html')
