from . models import Page

def pages_links(request):
    pages = Page.objects.first()
    return {'pages': pages}
    