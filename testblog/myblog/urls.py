from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views, feed

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^markdown/', include("django_markdown.urls")),
    url (r'^$', views.blogindex.as_view(), name="index"),
    url (r'^feed/$', feed.latest(), name="feed"),
	url (r'^(?P<slug>\S+)$', views.blogdetail.as_view(), name="entry_detail"),
)
