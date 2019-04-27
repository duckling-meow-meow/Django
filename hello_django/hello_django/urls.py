from django.conf.urls import include, url
from django.contrib import admin

from worker import views as tv
from worker import worker_url

# 这里是主路由
urlpatterns = [
    # Examples:
    # url(r'^$', 'hello_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^normal_map/', tv.do_normal_map),
    # worker_url是子路由
    url(r'^worker/', include(worker_url)),
    url(r'^with_param/(?P<year>[0-9]{4})/(?P<month>[0,1][0-9])', tv.with_param),
    url(r'book/(?:page-(?P<pn>\d+)/)$', tv.do_page_zh),
    url(r'^your_name/$', tv.external_param, {'name': "duckling"}),


]

