from django.contrib import admin

from .models import data_member,data_admin,hasil_kalkulasi,berita

admin.site.register(data_member)
admin.site.register(data_admin)
admin.site.register(hasil_kalkulasi)
admin.site.register(berita)
