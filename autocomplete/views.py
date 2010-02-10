#coding=utf8
from models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context import RequestContext
from django.shortcuts import render_to_response

def ajax_tag_autocomplete(request):
    if request.GET.has_key('q'):
        print request.GET['q']
        tags = Tag.objects.filter(name__icontains=request.GET['q'])[:10]
        return HttpResponse('\n'.join(tag.name for tag in tags))
    return HttpResponse()

def tags(request):
	if request.method == 'POST':
		tag_names = request.POST.get("tags","").split()
		for tag_name in tag_names:
			tag, dummy = Tag.objects.get_or_create(name=tag_name)
		return HttpResponseRedirect('/tags')
	else:
		tag_names = Tag.objects.all()
		variables = RequestContext(request, {'tags': tag_names })
		return render_to_response('tags.html', variables)