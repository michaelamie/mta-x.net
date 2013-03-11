from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.views.generic import RedirectView

admin.autodiscover()

urlpatterns = patterns('',
  url(r'^$', RedirectView.as_view(url='/blog/')),
  url(r'^blog/', include('blog.urls')),
  url(r'^trash/', include('trash.urls')),
  url(r'^admin/', include(admin.site.urls)),
  url(r'^grappelli/', include('grappelli.urls')),
)
