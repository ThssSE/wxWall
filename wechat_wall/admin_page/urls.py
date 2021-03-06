from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
                       url(r'^$', 'admin_page.views.home'),
                       url(r'^login/$', 'admin_page.views.login'),
                       url(r'^review/$', 'admin_page.views.review'),
                       url(r'^logout/$', 'admin_page.views.logout'),
                       url(r'^review_message/$', 'admin_page.views.review_message'),
                       url(r'^index/$', 'admin_page.views.index'),
                       url(r'^change_state/$', 'admin_page.views.change_review_state'),
                       url(r'^get_new_message/$', 'admin_page.views.get_new_message'),
                       url(r'^refresh_list/$', 'admin_page.views.refresh_review_list'),
                       url(r'^system_message/$', 'admin_page.views.post_system_message'),
                       )