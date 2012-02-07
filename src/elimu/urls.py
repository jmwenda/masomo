from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.views.generic import ListView,CreateView
from masomo.models import Subject,Chapter,Topic,Page,Content


from tastypie.api import Api
from masomo.api import EntryResource

from django.contrib import admin
admin.autodiscover()

from pinax.apps.account.openid_consumer import PinaxConsumer


handler500 = "pinax.views.server_error"


v1_api = Api(api_name='masomo')
v1_api.register(EntryResource())

urlpatterns = patterns("",
    url(r"^$", direct_to_template, {
        "template": "homepage.html",
    }, name="home"),
    url(r"^admin/invite_user/$", "pinax.apps.signup_codes.views.admin_invite_user", name="admin_invite_user"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^about/", include("about.urls")),
    url(r"^account/", include("pinax.apps.account.urls")),
    url(r"^openid/", include(PinaxConsumer().urls)),
    url(r"^subjects/$",ListView.as_view(model=Subject),name="curricula"),
    url(r'^subjects/create/', CreateView.as_view(model=Subject),name="subject-form"),
    url(r"^chapters/$",ListView.as_view(model=Chapter),name="chapters" ),
    url(r"^chapters/create/",CreateView.as_view(model=Chapter),name="chapter-form" ),
    url(r"^topics/$",ListView.as_view(model=Topic),name="topics" ),
    url(r"^topics/create/",CreateView.as_view(model=Topic),name="topic-form" ),
    url(r"^pages/$",ListView.as_view(model=Page),name="pages" ),
    url(r"^pages/create/",CreateView.as_view(model=Page),name="page-form" ),
    url(r"^content/$",ListView.as_view(model=Content),name="content" ),
    url(r"^content/create/",CreateView.as_view(model=Content),name="content-form" ),
    url(r"^profiles/", include("idios.urls")),
    url(r"^notices/", include("notification.urls")),
    url(r"^announcements/", include("announcements.urls")),
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^api/', include(v1_api.urls)),
)

if settings.SERVE_MEDIA:
    urlpatterns += patterns("",
        url(r"", include("staticfiles.urls")),
    )
