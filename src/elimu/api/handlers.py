from piston.handler import BaseHandler, AnonymousBaseHandler
from piston.utils import rc, require_mime, require_extended

from masomo.models import Device,Content

class DeviceHandler(BaseHandler):
	model = Device
        allowed_methods = ('GET',)
	anonymous = 'AnonymousDeviceHandler'
    	#fields = ('deviceidentifier', 'apikey', ('school', ('name',)), 'radius', ('school', ('longitude','latitude',)))



    	@classmethod
    	def resource_uri(cls, blogpost):
        	return ('device', [ 'xml', ])

    	def read(self, request, deviceid=None):
        	"""
        	Returns a blogpost, if `title` is given,
        	otherwise all the posts.
        
        	Parameters:
         	- `title`: The title of the post to retrieve.
        	"""
        	base = Device.objects
                if deviceid:
			device = Device.objects.get(deviceidentifier=deviceid)
			return device
			#return base.get(deviceidentifier=deviceid)
		else:
	            	return base.all()
class AnonymousDeviceHandler(DeviceHandler, AnonymousBaseHandler):
    """
    Anonymous entrypoint for blogposts.
    """
    fields = ('deviceidentifier', 'apikey', 'radius')
class ContentHandler(BaseHandler):
    model = Content
    allowed_methods = ('GET',)
    fields = ('subject')
    @classmethod
    def read(self,request):
        "return all the content on the platfrom, will need to add post handlers to deal with variables"
        base = Content.objects
        return base.get()
