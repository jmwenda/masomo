from tastypie.resources import ModelResource
from masomo.models import Content,Subject,Topic,Chapter,Page

class EntryResource(ModelResource):
    #subject = fields.ToManyField('masomo.api.SubjectResource', 'subject', related_name='entry')
    #subject = ForeignKey('masomo.api.SubjectResource','subject')
    class Meta:
        queryset = Content.objects.all()
        resource_name = 'content'

class SubjectResource(ModelResource):
    #entry = fields.ToOneField(EntryResource, 'entry')
    class Meta:
        queryset = Subject.objects.all()
        resource_name = 'subject'
class TopicResource(ModelResource):
    class Meta:
        queryset = Topic.objects.all()
        resource_name = 'topic'
class ChapterResource(ModelResource):
    class Meta:
        queryset = Chapter.objects.all()
        resource_name = 'chapter'

class PageResource(ModelResource):
    class Meta:
        queryset = Page.objects.all()
        resource_name = 'page'


