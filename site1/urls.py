from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

from site1.views import HomePageView, SignUpView, LoginView, LogoutView

urlpatterns = patterns('',
                       url(r'^$', HomePageView.as_view(), name="home"),
                       url(r'accounts/register/$', SignUpView.as_view(), name="signup"),
                       url(r'accounts/login/$', LoginView.as_view(), name="login"),
                       url(r'accounts/logout/$', LogoutView.as_view(), name="logout"),
                       url(r'^admin/', include(admin.site.urls)),
		       url(r'^talks/', include('talks.urls', namespace='talks')),
)
