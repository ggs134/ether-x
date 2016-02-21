""" Default urlconf for onther """

from django.conf.urls import include, patterns, url
from django.contrib import admin
from base import views
admin.autodiscover()


def bad(request):
    """ Simulates a server error """
    1 / 0

urlpatterns = [
    # Examples:
    # url(r'^$', 'onther.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^bad/$', bad),
    url(r'', include('base.urls'), name="home"),

    #wallet
    # url(r'^wallet/$',views.wallet, name="wallet"),
    url(r'^wallet/$', views.wallet, name="wallet"),
    url(r'^wallet/(?P<address>[a-zA-Z0-9]+)/$', views.wallet_detail, name="wallet_detail"),
    url(r'^wallet/add/', views.wallet_add, name="wallet_add"),

    #userlogin
    url(r'^accounts/login/$', views.login, name="accounts_login"),
    url(r'^accounts/auth/$', views.auth_view),
    url(r'^accounts/logout/$', views.logout),
    url(r'^accounts/invalid/$', views.invalid_login),

    #Transaction
    url(r'^eth/transaction/$', views.transaction_eth ,name="transaction_eth"),
]

# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'onther.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),
#     url(r'^admin/', include(admin.site.urls)),
#     url(r'^bad/$', bad),
#     url(r'', include('base.urls')),
#     url(r'^accounts/auth/$', views.auth_view),
#     url(r'^accounts/logout/$', views.logout),
#     url(r'^accounts/loggedin/$', views.loggedin),
#     url(r'^accounts/invalid/$', views.invalid_login),
# )

