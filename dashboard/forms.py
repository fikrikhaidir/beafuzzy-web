from django import forms
from django.contrib.auth import ( authenticate, get_user_model,
                                  login,logout,)
from django.contrib.auth.hashers import check_password
from .models import data_member,data_admin,berita,pesan_admin,pesan_user
from pagedown.widgets import PagedownWidget
from django.contrib.auth.models import User

#----------------------------------------- form untuk register atau mendaftar beasiswa ---------------------------
tahun_lahir_pilihan = [thn for thn in range(1945,2016)]
class isi_data_member(forms.ModelForm):
    TanggalLahir = forms.DateField(label='Tanggal Lahir',widget=forms.TextInput(attrs=
        {
            'class': 'datepicker'
        }))
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


class form_berita(forms.ModelForm):
    judul = forms.CharField(label='Judul Berita', error_messages={'required': 'Mohon diisi judul'})
    image = forms.ImageField(label='Sematkan Gambar', error_messages={'required': 'Mohon diisi gambar'})
    content = forms.CharField(widget=PagedownWidget())
    class Meta:
        model = berita
        fields = [
            'judul',
            'image',
            'content',
        ]

class form_pesan_admin(forms.ModelForm):
    subjek = forms.CharField(label='Subjek Pesan', error_messages={'required': 'Mohon diisi judul'})
    penerima = forms.ModelChoiceField(queryset=User.objects.all(),label='Kepada : ', error_messages={'required': 'Pesan Harus Memiliki Tujuan'})
    content = forms.CharField(label='Isi Pesan' ,widget=PagedownWidget())
    class Meta:
        model = pesan_admin
        fields = [
            'penerima',
            'subjek',
            'content',
        ]

class form_pesan_user(forms.ModelForm):
    subjek = forms.CharField(label='Subjek Pesan', error_messages={'required': 'Mohon diisi judul'})
    content = forms.CharField(label='Isi Pesan' ,widget=PagedownWidget())
    class Meta:
        model = pesan_user
        fields = [
            'subjek',
            'content',
        ]
