from django.db import models
from django.utils.translation import ugettext_lazy as _

from idios.models import ProfileBase


class Profile(ProfileBase):
    name = models.CharField(_("name"), max_length=50, null=True, blank=True)
    about = models.TextField(_("about"), null=True, blank=True)
    location = models.CharField(_("location"), max_length=40, null=True, blank=True)
    website = models.URLField(_("website"), null=True, blank=True, verify_exists=False)
    ACCOUNT_TYPE = ((u'Student', u'Student'),(u'Curriculum Developer', u'Curriculum Developer'))
    usergroup = models.CharField(choices=ACCOUNT_TYPE,max_length=20)

