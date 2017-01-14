from django.conf.urls import url
from django.contrib import admin
from . import views
from . import viewslong
urlpatterns = [
    url(r'^$', views.dashboard_home, name='home'),
    url(r'^profil/$', views.profile, name='profile'),
    url(r'^berita/$', views.berita, name='berita'),
    url(r'^pengumuman/$', views.pengumuman, name='pengumuman'),
    url(r'^timeline/$', views.timeline, name='timeline'),
    url(r'^pengaturan/$', views.pengaturan, name='pengaturan'),
    url(r'^adm/pendaftar/$', views.adm_listPendaftar, name='listPendaftar'),
    url(r'^adm/profile/$', views.adm_profile, name='adm_profile'),
    url(r'^adm/profile/(?P<id>\d+)/$', views.adm_profile_detail, name='adm_profile_detail'),
    url(r'^adm/profile/validasi/(?P<id>\d+)/$', viewslong.validasi_pendaftar, name='adm_validasi'),
    url(r'^adm/profile/terima/(?P<id>\d+)/$', viewslong.terima, name='terima'),


]
