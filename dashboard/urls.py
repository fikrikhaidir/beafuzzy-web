from django.conf.urls import url
from django.contrib import admin
from . import views,viewslong

urlpatterns = [
    url(r'^$', views.dashboard_home, name='home'),
    url(r'^berita/$', views.listBerita, name='berita'),
    url(r'^adm/detail_berita/(?P<id>\d+)/$', views.detail_berita, name='detail_berita'),
    url(r'^timeline/$', views.view_timeline, name='timeline'),
    url(r'^profil/$', views.profile, name='profile'),
    url(r'^profil/(?P<id>\d+)/$', views.edit_profile, name='edit_profile'),
    url(r'^pesan/$', views.pesan, name='pesan'),
    url(r'^pesan/baca/(?P<id>\d+)/$', views.baca_pesan, name='baca_pesan'),
    url(r'^pengaturan/$', views.pengaturan, name='pengaturan'),
    url(r'^faq/$', views.view_faq, name='faq'),
    url(r'^faq/(?P<id>\d+)/$', viewslong.del_faq, name='del_faq'),
    url(r'^cetakbuktidaftar/$', views.cetak_bukti_daftar, name='cetak_bukti_daftar'),


    url(r'^adm/pengumuman/$', viewslong.pengumuman, name='adm_pengumuman'),
    url(r'^adm/pendaftar/$', viewslong.adm_listPendaftar, name='listPendaftar'),
    url(r'^adm/profile/$', viewslong.adm_profile, name='adm_profile'),
    url(r'^adm/profile/(?P<id>\d+)/$', viewslong.adm_profile_detail, name='adm_profile_detail'),
    url(r'^adm/profile/validasi/(?P<id>\d+)/$', viewslong.validasi_pendaftar, name='adm_validasi'),
    url(r'^adm/profile/terima/(?P<id>\d+)/$', viewslong.terima, name='terima'),
    url(r'^adm/pesan/$', viewslong.adm_pesan, name='adm_pesan'),
    url(r'^adm/berita/$', viewslong.adm_berita, name='adm_berita'),
    url(r'^adm/cetak/$', viewslong.cetakTest, name='adm_cetak'),
    url(r'^adm/edit_faq/(?P<id>\d+)/$', viewslong.edit_faq, name='edit_faq'),

]
