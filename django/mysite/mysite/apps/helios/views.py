from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import RequestContext
# Create your views here.
def dispatch(request,name):

	return render_to_response("helios/"+name+".html", RequestContext(request, {}))

def index(request):

	return dispatch(request,'index')
# Create your views here.
