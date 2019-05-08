"""smartlink URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static



from apps.smartlink import views

from django.urls import reverse_lazy
from django.contrib.auth.views import (
    
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

#from django.contrib.auth.views import (
#    login, logout, password_reset, password_reset_done, password_reset_confirm,
#    password_reset_complete
#)

app_name = "smartlink"
urlpatterns = [
    
    url(r'^admin/', admin.site.urls),
    url(r'^evento/(?P<pk>\d+)/$',views.evento,name="evento"),
    url(r'^historial/(?P<pk>\d+)/$',views.agregareventoacliente,name="agregareventoacliente"),
    url(r'^historial/(?P<pk>\d+)/$',views.quitarevento,name="quitarevento"),
    
    url(r'^$',views.home,name="index"),
    #url(r'^email-users/$',views.SendUserEmails.as_view(),name="email"),
    #url(r'^login/$',views.login,name="login"),
    #url(r'^registro/$',views.registro,name="registro"),
    url(r'^login/$', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    # LoginView.as_view(template_name='accounts/login.html'), name='login'),
    #url(r'^logout/$', LogoutView.as_view(next_page=reverse_lazy('login')), name='logout'),
    url(r'^logout/$', LogoutView.as_view(next_page=reverse_lazy('index')), name='logout'),
    url(r'^historial/$', views.historial, name='historial'),
    #url(r'^login/$', login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    #url(r'^profile/(?P<pk>\d+)/$', views.view_profile, name='view_profile_with_pk'),
    url(r'^profile/edit_profile/$', views.edit_profile, name='edit_profile'),
    url(r'^profile/edit_profile/password/$', views.change_password, name='change_password'),

    #url(r'^reset-password/$', password_reset, {'template_name': 'accounts/reset_password.html', 'post_reset_redirect': 'accounts:password_reset_done', 'email_template_name': 'accounts/reset_password_email.html'}, name='reset_password'),

    #url(r'^reset-password/done/$', password_reset_done, {'template_name': 'accounts/reset_password_done.html'}, name='password_reset_done'),

    #url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, {'template_name': 'accounts/reset_password_confirm.html', 'post_reset_redirect': 'accounts:password_reset_complete'}, name='password_reset_confirm'),

    #url(r'^reset-password/complete/$', password_reset_complete,{'template_name': 'accounts/reset_password_complete.html'}, name='password_reset_complete')
    #url(r'^', include('smartlink.urls')),






]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)