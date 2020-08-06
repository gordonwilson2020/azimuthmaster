from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('team', views.team, name='team'),
    path('business', views.business, name='business'),
    path('marketing', views.marketing, name='marketing'),
    path('permitting', views.permitting, name='permitting'),
    path('alberta', views.alberta, name='alberta'),
    path('bc', views.bc, name='bc'),
    path('manitoba', views.manitoba, name='manitoba'),
    path('newbrunswick', views.newbrunswick, name='newbrunswick'),
    path('newfoundland', views.newfoundland, name='newfoundland'),
    path('northwest', views.northwest, name='northwest'),
    path('novascotia', views.novascotia, name='novascotia'),
    path('nunavut', views.nunavut, name='nunavut'),
    path('ontario', views.ontario, name='ontario'),
    path('princeedward', views.princeedward, name='princeedward'),
    path('quebec', views.quebec, name='quebec'),
    path('saskatchewan', views.saskatchewan, name='saskatchewan'),
    path('yukon', views.yukon, name='yukon'),
    path('businesshub', views.businesshub, name='businesshub'),
    path('businessplan', views.businessplan, name='businessplan'),
    path('chat', views.chat, name='chat'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('disclaimer', views.disclaimer, name='disclaimer'),
    path('marketinghub', views.marketinghub, name='marketinghub'),
    path('privacy', views.privacy, name='privacy'),
    path('profile', views.profile, name='profile'),
    path('terms', views.terms, name='terms'),
    path('sopbuilder', views.sopbuilder, name='sopbuilder'),
]







