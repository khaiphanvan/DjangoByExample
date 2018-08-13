from django.http import HttpResponseBadRequest
import logging

logger = logging.getLogger(__name__)

def ajax_required(f):
    def wrap(request, *args, **kwargs):
        if not request.is_ajax():
            logger.error('Khong phai ajax')
            return HttpResponseBadRequest()
        logger.error('ajax')
        return f(request, *args, **kwargs)
    wrap.__doc__=f.__doc__
    wrap.__name__=f.__name__
    return wrap