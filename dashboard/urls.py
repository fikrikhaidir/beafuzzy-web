from django.conf.urls import url
from django.contrib import admin
from . import views,viewslong

urlpatterns = [
    url(r'^$', views.dashboard_home, name='home'),
    url(r'^berita/$', views.listBerita, name='berita'),
    url(r'^timeline/$', views.timeline, name='timeline'),
    url(r'^profil/$', views.profile, name='profile'),
    url(r'^pesan/$', views.pesan, name='pesan'),
    url(r'^pengaturan/$', views.pengaturan, name='pengaturan'),
    url(r'^faq/$', views.faq, name='faq'),


    url(r'^adm/pengumuman/$', viewslong.pengumuman, name='adm_pengumuman'),
    url(r'^adm/pendaftar/$', viewslong.adm_listPendaftar, name='listPendaftar'),
    url(r'^adm/profile/$', viewslong.adm_profile, name='adm_profile'),
    url(r'^adm/profile/(?P<id>\d+)/$', viewslong.adm_profile_detail, name='adm_profile_detail'),
    url(r'^adm/profile/validasi/(?P<id>\d+)/$', viewslong.validasi_pendaftar, name='adm_validasi'),
    url(r'^adm/profile/terima/(?P<id>\d+)/$', viewslong.terima, name='terima'),
    url(r'^adm/berita/$', viewslong.adm_berita, name='adm_berita'),

]
