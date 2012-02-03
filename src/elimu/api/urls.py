#create your views here.
from django.conf.urls.defaults import *
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
from piston.doc import documentation_view

from api.handlers import *


device = Resource(handler=DeviceHandler)
content = Resource(handler=ContentHandler)

urlpatterns = patterns('',
    url(r'^posts/$', device),
    url(r'^posts/(?P<emitter_format>.+)/$', device),
    url(r'^posts\.(?P<emitter_format>.+)', device, name='device'),
    url(r'^content/(?P<emitter_format>.+)/$', content),
    # automated documentation
    #url(r'^$', documentation_view),
)

