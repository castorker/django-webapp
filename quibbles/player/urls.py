from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import home, new_invite, accept_invite

urlpatterns = [
    path('home', home, name="player_home"),
    path('login', LoginView.as_view(template_name="player/login_form.html"), name="player_login"),
    path('logout', LogoutView.as_view(), name="player_logout"),
    path('new_invite', new_invite, name="player_new_invite"),
    path(r'accept_invite/(?P<id>\d+)/$', accept_invite, name="player_accept_invite")
]
