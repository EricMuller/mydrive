from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render_to_response
from django.shortcuts import RequestContext
from django.shortcuts import render


# def test(request):
#     return dispatch(request, 'test')

def hello(request):
    return HttpResponse("Hello world")


def note(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    # dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>note %s</body></html>" % (offset)
    return HttpResponse(html)


def site(request):

    return render_to_response("index.html",
                              RequestContext(request, {}))


# def page_not_found(request):
# Dict to pass to template, data could come from DB query
# import pdb
# pdb.set_trace()
#     values_for_template = {}
#     return render(request, 'index.html', values_for_template, status=404)


# def server_error(request):
# Dict to pass to template, data could come from DB query
#     values_for_template = {}
#     return render(request, 'index.html', values_for_template, status=500)


# def bad_request(request):
# Dict to pass to template, data could come from DB query
#     values_for_template = {}
#     return render(request, 'index.html', values_for_template, status=400)


# def permission_denied(request):
# Dict to pass to template, data could come from DB query
#     values_for_template = {}
#     return render(request, 'index.html', values_for_template, status=403)
