from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
import simplejson
from settings.common import TEST_MODE


def create_photo(request):
    # request.meta.contenttype = 'application/x-www-form-urlencoded; charset=utf-8'
    if request.method == 'POST':
        dic = simplejson.loads(request.body)
        return HttpResponse(simplejson.dumps(dic), mimetype='application/json')

    ctx = {
        'test_mode': TEST_MODE
    }
    return render_to_response('tests/create_photo.html', ctx, context_instance=RequestContext(request))