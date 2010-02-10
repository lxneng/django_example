from django.conf.urls.defaults import *
import os.path
from autocomplete.views import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
site_media = os.path.join(
    os.path.dirname(__file__), 'site_media'
)
urlpatterns = patterns('',
    (r'^autocomplete/$', ajax_tag_autocomplete),
    (r'^tags/$', tags),
    # (r'^admin/', include(admin.site.urls)),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': site_media }),
)
