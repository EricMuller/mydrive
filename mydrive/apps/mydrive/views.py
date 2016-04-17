# from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse
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


def dispatch(request, name):
    return render_to_response("mydrive/" + name + ".html",
                              RequestContext(request, {}))


def partials(request, name):
    return render_to_response("mydrive/partials/" + name + ".html",
                              RequestContext(request, {}))


def partials2(request, name, name2):
    return render_to_response("mydrive/partials/" + name + "/" + name2 + ".html",
                              RequestContext(request, {}))


def partials3(request, name, name2, name3):
    return render_to_response("mydrive/partials/" + name + "/" +
                              name2 + "/" + name3 + ".html",
                              RequestContext(request, {}))


def login(request):
    return dispatch(request, 'login')


# @login_required( login_url='/ged/#/login')
def index(request):
    return dispatch(request, 'index')
