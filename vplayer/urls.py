from django.urls import path,include
from vplayer import views

urlpatterns = [
    path('',views.index , name="index"),
    path('vplayer',views.vplayer , name="vplayer"),
    path('aplayer',views.aplayer , name="aplayer"),

    path('signup',views.signup , name="signup"),
    path('login',views.ulogin , name="login"),
    path('logout',views.ulogout , name="logout"),

    path('uprofile',views.uprofile , name="uprofile"),

    
    path('addvideo',views.addvideo , name="addvideo"),
    path('video/<int:sno>',views.video , name="video"),
    path('onvhide/<int:sno>',views.vhide , name="onhide"),
    path('onvunhide/<int:sno>',views.vunhide , name="onunhide"),
    path('onvdelete/<int:sno>',views.vdelete , name="ondelete"),
    path('vcomment/<int:sno>',views.vcomment , name='vcomment'),


    path('addaudio',views.addaudio , name="addaudio"),
    path('onahide/<int:sno>',views.ahide , name="onhide"),
    path('onaunhide/<int:sno>',views.aunhide , name="onunhide"),
    path('onadelete/<int:sno>',views.adelete , name="ondelete"),
]
