from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.utils import timezone
import datetime

class data_member(models.Model):
    akun = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    nama = models.CharField(null=False, max_length=35, default='')
    avatar = models.ImageField(upload_to='upload/avatar,',null=True,blank=True,verbose_name='avatar',default='' )
    fakultas = models.CharField(null=False, max_length=40, default='')
    telepon = models.CharField(null=True,blank=True,max_length=18,default='')
    prodi = models.CharField(null=False, max_length=40, default='')
    nim = models.CharField(null=False, max_length=10, default='', verbose_name='NIM')
    ktm = models.ImageField(upload_to='upload/ktm', default='', verbose_name='KTM')
    alamat = models.TextField(null=False, max_length=300, default='')
    TanggalLahir = models.DateField(null=False, default='', verbose_name='Tanggal Lahir (ex : 1995-01-05)')
    semester = models.IntegerField(null=False, default='', verbose_name='Semester')
    ipk = models.FloatField(null=False, max_length=5, default='',verbose_name='IPK')
    transkrip = models.ImageField(upload_to='upload/transkrip', default='', verbose_name='Transkrip Nilai')
    tan = models.FloatField(null=False, default='', verbose_name='Tanggungan Orang Tua')
    bukti_tan = models.ImageField(null=False, default='',upload_to='upload/bukti_tan',verbose_name='Bukti Tanggungan Orang Tua. ex : Kartu Keluarga')
    pot = models.FloatField(null=False, default='', verbose_name='Pendapatan Orang Tua/Bulan (Rp)')
    bukti_pot =models.ImageField(null=False, default='',upload_to='upload/bukti_pot',verbose_name='Bukti Pendapatan Orang Tua. Ex : Slip Gaji')
    pre_choices_pre = (
        (0.55, '---Tidak Ada---'),
        (1.75 , 'Regional'),
        (3.45 , 'Nasional'),
        (5.5 , 'Internasional'),
    )
    pre = models.FloatField(null=False, default='', choices=pre_choices_pre, verbose_name='Prestasi (Pilih prestasi yang paling tinggi)')
    bukti_prestasi = models.ImageField(null=True,blank=True,upload_to='upload/bukti_prestasi', default='', verbose_name='Bukti Prestasi')
    pre_choices_org = (
        (0.55, '---Tidak Ada---'),
        (1.75 , 'Regional'),
        (3.45 , 'Nasional'),
        (5.5 , 'Internasional'),
    )
    org = models.FloatField(null=False, default='', choices=pre_choices_org, verbose_name='Organisasi (Pilih organisasi yang tertinggi)')
    bukti_organisasi = models.ImageField(null=True,blank=True,upload_to='upload/bukti_organisasi', default='',verbose_name='Bukti Organisasi')
    tgl_daftar = models.DateField(null=False, default='')
    daftar = models.BooleanField(default=False)
    valid = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s' % self.nama

    def get_absolute_url(self):
        return reverse("accounts:detail",kwargs={"id" : self.id})



class data_admin(models.Model):
    akun = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    avatar = models.ImageField(upload_to='upload/avatar,',null=True,blank=True,verbose_name='avatar',default='')
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
    tunggu = models.BooleanField(default=True)
    diterima = models.BooleanField(default=False)


    def __unicode__(self):
        return '%s' % self.nama

class berita(models.Model):
    judul = models.CharField(default='', max_length=200,null=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    slug = models.SlugField(unique=True,max_length=255)
    image = models.ImageField(upload_to='upload/berita', default='')
    content = models.TextField(null=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return '%s' % self.judul

    class Meta:
        ordering = ["-timestamp"]

    def get_absolute_url(self):
        return reverse("dashboard:detail_berita", kwargs={"slug": self.slug})

def create_slug(instance, new_slug=None):
    slug = slugify(instance.judul)
    if new_slug is not None:
        slug = new_slug
    qs = berita.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_berita_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
pre_save.connect(pre_save_berita_receiver,sender=berita)

class pesan_admin(models.Model):
    subjek = models.CharField(default='', max_length=120,null=False)
    penerima = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=False)
    content = models.TextField(null=False)
    dibaca = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return '%s' % self.penerima +' | '+ self.subjek
    class Meta:
        ordering = ["-timestamp"]

class pesan_user(models.Model):
    subjek = models.CharField(default='', max_length=120,null=False)
    pengirim = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    content = models.TextField(null=False)
    dibaca = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return '%s' % self.pengirim +' | '+ self.subjek
    class Meta:
        ordering = ["-timestamp"]

class timeline(models.Model):
    j_pendaftaran = models.CharField(default='', max_length=120,null=False)
    j_review = models.CharField(default='', max_length=120,null=False)
    j_seleksi = models.CharField(default='', max_length=120,null=False)
    j_pengumuman = models.CharField(default='', max_length=120,null=False)
    j_penerimaan = models.CharField(default='', max_length=120,null=False)
    c_pendaftaran = models.TextField(null=False,max_length=320,default='')
    c_review = models.TextField(null=False,max_length=320,default='')
    c_seleksi = models.TextField(null=False,max_length=320,default='')
    c_pengumuman = models.TextField(null=False,max_length=320,default='')
    c_penerimaan = models.TextField(null=False,max_length=320,default='')
    t_pendaftaran = models.TextField(null=False,max_length=45,default='')
    t_review = models.TextField(null=False,max_length=45,default='')
    t_seleksi = models.TextField(null=False,max_length=45,default='')
    t_pengumuman = models.TextField(null=False,max_length=45,default='')
    t_penerimaan = models.TextField(null=False,max_length=45,default='')
    tahun_penerimaan = models.CharField(null=False,blank=False, max_length=4,default=0)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False,null=True)

    def __unicode__(self):
        return 'Tanggal Penting & Event'

class faq(models.Model):
    pertanyaan = models.CharField(default='', max_length=105,null=False)
    jawaban = models.TextField(null=False, max_length=1500, default='')
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True,null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False,null=True)

    def __unicode__(self):
        return '%s' % self.pertanyaan
    class Meta:
        ordering = ["-timestamp"]
