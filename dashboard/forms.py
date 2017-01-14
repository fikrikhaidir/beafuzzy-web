from django import forms
from django.contrib.auth import ( authenticate, get_user_model,
                                  login,logout,)
from django.contrib.auth.hashers import check_password
from .models import data_member,data_admin

#----------------------------------------- form untuk register atau mendaftar beasiswa ---------------------------
tahun_lahir_pilihan = [thn for thn in range(1980,2016)]
class isi_data_member(forms.ModelForm):
    TanggalLahir = forms.DateField(
        widget=forms.SelectDateWidget(years=tahun_lahir_pilihan)
    )
    class Meta:
        model = data_member
        fields = [
            "nama",
            "fakultas",
            "prodi",
            "nim",
            "ktm",
            "alamat",
            "TanggalLahir",
            "semester",
            "ipk",
            "transkrip",
            "tan",
            "pot",
            "pre",
            "bukti_prestasi",
            "org",
            "bukti_organisasi",
        ]

class isi_data_admin(forms.ModelForm):
    TanggalLahir = forms.DateField(
        widget=forms.SelectDateWidget(years=tahun_lahir_pilihan)
    )
    class Meta:
        model = data_admin
        fields = [
            "nama",
            "jabatan",
            "fakultas",
            "prodi",
            "nik",
            "alamat",
            "TanggalLahir",
        ]
# class perhitungan(forms.Form):
