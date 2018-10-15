from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
    url(r'^feed/$', views.index, name = 'index'),
    url(r'^login/$', views.login, name = 'login'),
    url(r'^logout/$', views.logout_view, name = 'logout'),
    url(r'^work/$', views.work, name = 'work'),
    url(r'^news/$', views.news, name = 'news'),
    url(r'^settings/$', views.settings, name = 'news'),
    url(r'^picture/$', views.picture, name = 'news'),
    url(r'^group/$', views.group, name = 'group'),
    url(r'^profile/(?P<profile_id>[0-9]+)/$', views.profile, name = 'login'),
    # url(r'^(?P<order_id>[0-9]+)/$', views.order, name='order'),
    # url(r'^registrations/$', views.registrations, name = 'register'),
    # url(r'^login/$', views.login, name = 'login'),
    # url(r'^logout/$', views.logout, name = 'logout'),
    # url(r'^loginned/$', views.logginned, name = 'loginok'),
    # url(r'^order/(?P<edit_order_id>[0-9]+)/$', views.edit, name='edit'),
    # url(r'^editprofile/(?P<edit_profile_id>[0-9]+)/$', views.editprofile,name='editprofile'),
    # url(r'^profile/(?P<views_profile_id>[0-9]+)/$', views.profile,name='profile')
]