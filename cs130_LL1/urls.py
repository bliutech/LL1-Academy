"""cs130_LL1 URL Configuration

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
from django.urls import include, re_path
from django.contrib import admin

import LL1_Academy.views.practice as practice
import LL1_Academy.views.tutorial as tutorial
import LL1_Academy.views.views as views
import LL1_Academy.views.stats as stats
import LL1_Academy.views.userProfile as user_profile


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', views.index),
    re_path(r'^index$', views.index),
    re_path(r'^about$', views.about),
    re_path(r'^practice', practice.practice),
    re_path(r'^tutorial$', tutorial.tutorial),
    re_path(r'^get_question$', practice.get_question),
    re_path(r'^check_answer$', practice.check_answer),
    re_path(r'^give_up$', practice.give_up),
    re_path(r'^log_skip_grammar$', stats.log_skip_grammar),
    re_path(r'^profile$', user_profile.profile),
    re_path(r'^accounts/disconnect_account$', user_profile.disconnect_account),
    re_path(r'^accounts/social/connections/$', user_profile.profile),
    re_path(r'^accounts/social/signup/$', user_profile.login_duplicate),
    re_path(r'^accounts/', include('allauth.urls')),
]

handler404='LL1_Academy.views.views.handler404'
handler500='LL1_Academy.views.views.handler500'
handler400='LL1_Academy.views.views.handler400'
