from django import forms
from django.contrib.auth import ( authenticate, get_user_model,
                                  login,logout,)
from django.contrib.auth.hashers import check_password
from .models import data_member,data_admin,berita,pesan_admin,pesan_user,timeline,faq
from pagedown.widgets import PagedownWidget
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm

#----------------------------------------- form untuk register atau mendaftar beasiswa ---------------------------
tahun_lahir_pilihan = [thn for thn in range(1945,2016)]
class isi_data_member(forms.ModelForm):
    TanggalLahir = forms.DateField(label='Tanggal Lahir',widget=forms.TextInput(attrs=
        {
            'class': 'datepicker'
        }))
    avatar = forms.ImageField(label=' Avatar (Dimensi Optimal = Rasio 1:1 / 200 x 200 px)')

    class Meta:
        model = data_member
        fields = [
            "nama",
            "avatar",
            "fakultas",
            "prodi",
            "telepon",
            "nim",
            "ktm",
            "alamat",
            "TanggalLahir",
            "semester",
            "ipk",
            "transkrip",
            "tan",
            "bukti_tan",
            "pot",
            "bukti_pot",
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
            "avatar",
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
    content = forms.CharField(widget=forms.Textarea)
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

class form_timeline_pendaftaran(forms.ModelForm):
    class Meta:
        model = timeline
        fields = [
            'j_pendaftaran',
            't_pendaftaran',
            'c_pendaftaran',
        ]

class form_timeline_review(forms.ModelForm):
    class Meta:
        model = timeline
        fields = [
            'j_review',
            't_review',
            'c_review',
        ]

class form_timeline_seleksi(forms.ModelForm):
    class Meta:
        model = timeline
        fields = [
            'j_seleksi',
            't_seleksi',
            'c_seleksi',
        ]

class form_timeline_pengumuman(forms.ModelForm):
    class Meta:
        model = timeline
        fields = [
            'j_pengumuman',
            't_pengumuman',
            'c_pengumuman',
        ]

class form_timeline_penerimaan(forms.ModelForm):
    class Meta:
        model = timeline
        fields = [
            'j_penerimaan',
            't_penerimaan',
            'c_penerimaan',
        ]

class form_faq(forms.ModelForm):
    class Meta:
        model = faq
        fields= [
            'pertanyaan',
            'jawaban',
        ]

class ganti_password(PasswordChangeForm):
    # old_password = forms.CharField(widget=forms.PasswordInput, label='Password Lama', error_messages={'required':'Mohon diisi (Nama Depan) Anda'})
    # # new_password = forms.CharField(widget=forms.PasswordInput, label='Password Baru', error_messages={'required':'Mohon diisi (Nama Depan) Anda'})
    # # new_confirmation_password = forms.CharField(widget=forms.PasswordInput, label='Konfirmasi Password', error_messages={'required':'Mohon diisi (Nama Depan) Anda'})

    class Meta :
        model = User
        fields = [
            'old_password',
            'new_password',
            'new_confirmation_password',
        ]
