from django.contrib import admin
from masomo.models import *


class ChapterInline(admin.TabularInline):
    model = Chapter
    extra = 1
class SubjectAdmin(admin.ModelAdmin):
    #fieldsets = [(None,               {'fields': ['name'],['description']})]
    inlines = [ChapterInline]
class TopicInline(admin.TabularInline):
    model = Topic
    extra = 1
class TopicAdmin(admin.ModelAdmin):
    #fieldsets = [(None,               {'fields': ['name'],['description']})]
    inlines = [TopicInline]
admin.site.register(Subject,SubjectAdmin)
admin.site.register(Chapter,TopicAdmin)
admin.site.register(Topic)
admin.site.register(Curriculumdev)
admin.site.register(ContentType)
admin.site.register(Constraint)
admin.site.register(Content)
admin.site.register(Device)
admin.site.register(School)
admin.site.register(County)
admin.site.register(Radius)

