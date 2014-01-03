from django.shortcuts import render


def load_template(request, template_path):
    ''' Render the static template <template_path>.html

    **Arguments:**
        *template_path*: The template filename without the extension

    **Returns:**
        The contents of the file <template_path.html> rendered
    '''

    return render(request, template_path + '.html')
