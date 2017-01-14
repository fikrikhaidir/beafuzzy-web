from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

class data_member(models.Model):
    akun = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    nama = models.CharField(null=False, max_length=35, default='')
    fakultas = models.CharField(null=False, max_length=40, default='')
    prodi = models.CharField(null=False, max_length=40, default='')
    nim = models.CharField(null=False, max_length=10, default='', verbose_name='NIM')
    ktm = models.ImageField(upload_to='upload/ktm', default='', verbose_name='KTM')
    alamat = models.TextField(null=False, max_length=300, default='')
    TanggalLahir = models.DateField(null=False, default='', verbose_name='Tanggal Lahir (ex : 1995-01-05)')
    semester = models.IntegerField(null=False, default='', verbose_name='Semester')
    ipk = models.FloatField(null=False, max_length=5, default='',verbose_name='IPK')
    transkrip = models.ImageField(upload_to='upload/transkrip', default='', verbose_name='Transkrip Nilai')
    tan = models.FloatField(null=False, default='', verbose_name='Tanggungan Orang Tua')
    pot = models.FloatField(null=False, default='', verbose_name='Pendapatan Orang Tua/Bulan (Rp)')
    pre_choices_pre = (
        (0.55, '---Tidak Ada---'),
        (1.75 , 'Regional'),
        (3.45 , 'Nasional'),
        (5.5 , 'Internasional'),
    )
    pre = models.FloatField(null=False, default='', choices=pre_choices_pre, verbose_name='Prestasi (Pilih prestasi yang paling tinggi)')
    bukti_prestasi = models.ImageField(upload_to='upload/bukti_prestasi', default='', verbose_name='Bukti Prestasi')
    pre_choices_org = (
        (0.55, '---Tidak Ada---'),
        (1.75 , 'Regional'),
        (3.45 , 'Nasional'),
        (5.5 , 'Internasional'),
    )
    org = models.FloatField(null=False, default='', choices=pre_choices_org, verbose_name='Organisasi (Pilih organisasi yang tertinggi)')
    bukti_organisasi = models.ImageField(upload_to='upload/bukti_organisasi', default='',verbose_name='Bukti Organisasi')
    tgl_daftar = models.DateField(null=False, default='')
    daftar = models.BooleanField(default=False)
    valid = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s' % self.nama

    def get_absolute_url(self):
        return reverse("accounts:detail",kwargs={"id" : self.id})



class data_admin(models.Model):
    akun = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    nama = models.CharField(null=False, max_length=35, default='')
    jabatan = models.CharField(null=False, max_length=40, default='')
    fakultas = models.CharField(null=False, max_length=40, default='')
    prodi = models.CharField(null=False, max_length=40, default='')
    nik = models.CharField(null=False, max_length=10, default='', verbose_name='NIK')
    alamat = models.TextField(null=False, max_length=300, default='')
    TanggalLahir = models.DateField(null=False, default='', verbose_name='Tanggal Lahir (ex : 1995-01-05)')
    tgl_daftar = models.DateField(null=False, default='')
    daftar = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s' % self.nama

    def get_absolute_url(self):
        return reverse("dashboard:listPendaftar",kwargs={"id" : self.id})



class hasil_kalkulasi(models.Model):
    akun = models.IntegerField(null=False, blank=True,default=0)
    nama = models.CharField(null=False, max_length=35, default='')
    nim = models.CharField(null=False, max_length=10, default='')
    fakultas=models.CharField(null=False, max_length=50, default='')
    prodi= models.CharField(null=False,max_length=50,default='')
    tan = models.FloatField(null=False, default=0)
    pot = models.FloatField(null=False, default=0)
    pre = models.FloatField(null=False, default=0)
    org = models.FloatField(null=False, default=0)
    ipk = models.FloatField(null=False, default=0)
    rek = models.FloatField(null=True, default=0)
    diterima = models.BooleanField(default=False)


    def __unicode__(self):
        return '%s' % self.nama
