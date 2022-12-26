from .models import *

def menu_links(request):
    links = Villa.objects.all()
    return dict(links=links)