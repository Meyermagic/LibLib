from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'LibLib.views.home', name='home'),
    # url(r'^LibLib/', include('LibLib.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'LibLibSite.views.home', name='home'),

    url(r'^category/(?P<category_id>\d+)/$', 'LibLibSite.views.category_browse', name='category_browse'),
    url(r'^algorithms/(?P<algorithm_id>\d+)/$', 'LibLibSite.views.algorithm_browse', name='algorithm_browse'),
    url(r'^algorithms/(?P<algorithm_id>\d+)/(?P<impl_id>\d+)/$', 'LibLibSite.views.alg_impl_view', name='alg_implementation_view'),

    url(r'^structures/(?P<structure_id>\d+)/$', 'LibLibSite.views.structure_browse', name='structure_browse'),
    url(r'^structures/(?P<structure_id>\d+)/(?P<impl_id>\d+)/$', 'LibLibSite.views.struct_impl_view', name='struct_implementation_view'),

    (r'^accounts/', include('registration.urls')),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/profile/$', 'LibLibSite.views.profile', name='user_profile'),
    url(r'^accounts/(?P<username>\W+)/$', 'LibLibSite.views.profile_other', name='user_profile_other'),
)
