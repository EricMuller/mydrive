
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import RequestContext

from django.template import Context
from django.template.loader import get_template


def home(request):
    return render_to_response("index.html", RequestContext(request, {}))


def index(request):
    #now = datetime.datetime.now()
    #html = "<html><body>It is now %s.</body></html>" % now
    #return HttpResponse(html)
#    now = datetime.datetime.now()
#    t = get_template('notes/index.html')
#    html = t.render(Context({'current_date': now}))
#    return HttpResponse(html)
     return render_to_response("default/index.html", RequestContext(request, {}))   


     