
# from django.http import HttpResponse
# from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import RequestContext

# from django.template import Context
# from django.template.loader import get_template


def test(request):
    # now = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    # return HttpResponse(html)
    # now = datetime.datetime.now()
    # t = get_template('ged/index.html')
    # html = t.render(Context({'current_date': now}))
    # return HttpResponse(html)
    return dispatch(request, 'test')

def material(request):
    # now = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    # return HttpResponse(html)
    # now = datetime.datetime.now()
    # t = get_template('ged/index.html')
    # html = t.render(Context({'current_date': now}))
    # return HttpResponse(html)
    return dispatch(request, 'material')

def dispatch(request,  name):
    return render_to_response("ged/"+ name + ".html",
                              RequestContext(request, {}))

def partials(request, name):
    return render_to_response("ged/partials/" + name + ".html",
                              RequestContext(request, {}))

def index(request):

    return dispatch(request, 'index')
