from django.http import HttpResponse
from django.template import loader


def home(request):
    template = loader.get_template('myhome.html')
    context = {
        'home': 'home',
    }
    return HttpResponse(template.render(context, request))

