from django.conf.urls.defaults import *

urlpatterns = patterns('simpleapi.views',
    url(r'^token/new.json$', 'token_new', name="api_token_new"),
    url(r'^token/(?P<token>.{24})/(?P<user>\d+).json$', 'token', name="api_token"),
)
