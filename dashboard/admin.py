from django.contrib import admin

from .models import data_member,data_admin,hasil_kalkulasi,berita,pesan_admin,pesan_user

admin.site.register(data_member)
admin.site.register(data_admin)
admin.site.register(hasil_kalkulasi)
admin.site.register(berita)
admin.site.register(pesan_admin)
admin.site.register(pesan_user)
