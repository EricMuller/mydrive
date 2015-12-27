from django.http import HttpResponse

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import RequestContext


def hello(request):
    return HttpResponse("Hello world")

def note(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
 #   dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>note %s</body></html>" % (offset)
    return HttpResponse(html)    

def infusion(request):
    
    return render_to_response("infusion/index.html", RequestContext(request, {}))    

def digitalworld(request):
    
    return render_to_response("digitalworld/index.html", RequestContext(request, {}))    

def bliss(request):
    
    return render_to_response("bliss/index.html", RequestContext(request, {}))  

def site(request):
    
    return render_to_response("index.html", RequestContext(request, {}))  
