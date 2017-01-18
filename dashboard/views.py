from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse, Http404,HttpRequest
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import isi_data_member,isi_data_admin,form_berita,form_pesan_admin,form_pesan_user
from .models import data_member,data_admin,hasil_kalkulasi,berita,pesan_admin,pesan_user
from django.utils import timezone
from django import template
import datetime
from django.db import connection
from django.db.models import Q
from django.contrib.gis.geoip2 import GeoIP2


@login_required
def dashboard_home(request):
    kota = GeoIP2().city('36.73.70.173')
    # kotaa = request.META.get('HTTP_X_FORWARDED_FOR')
    # kota = GeoIP2().city(kotaa)

    print request.META.get('REMOTE_ADDR')
    print request.META.get('REMOTE_HOST')
    kota,provinsi,negara = kota['city'],kota['region'],kota['country_name']
    waktu = datetime.datetime.now()
    tahun,bulan,tanggal = waktu.year,waktu.month,waktu.day
    jam, menit = waktu.hour, waktu.minute
    arr_bulan = {'1':'Jan','2':'Feb','3':'Mar','4':'Apr','5':'Mei','6':'Jun','7':'Jul','8':'Agu','9':'Sep','10':'Okt','11':'Nov','12':'Des'}
    bulan = arr_bulan[str(bulan)]
    salam,tanda ='',''
    if waktu.hour < 12 :
        salam = 'Pagi'
        tanda = 'AM'
    elif waktu.hour < 18 and waktu.hour >= 12 :
        salam = 'Siang'
        tanda = 'PM'
    elif waktu.hour >=18:
        salam = 'Malam'
        tanda = 'PM'
    context ={
        'salam':salam,
        'jam': jam,'menit': menit,'tahun':tahun,'bulan':bulan,'tanggal':tanggal,
        'tanda':tanda,
        'kota':kota,'provinsi':provinsi,'negara':negara,
    }

    akun = request.user
    if akun.is_superuser:
        data = data_admin.objects.filter(akun=akun)
        if data:
            user = data_admin.objects.get(akun=akun)
            request.session['nama']=user.nama
            request.session['fakultas']=user.fakultas
            context['fakultas']=request.session['fakultas']
        else:
            request.session['nama']=akun.username
            request.session['fakultas']=''

    else:
        data = data_member.objects.filter(akun=akun)
        if data:
            user = data_member.objects.get(akun=akun)
            request.session['nama']=user.nama
            request.session['fakultas']=user.fakultas
            context['fakultas']=request.session['fakultas']
        else:
            request.session['nama']=akun.username
            request.session['fakultas']=''


    context['username']=request.session['nama']
    return render(request,"dash/dash_home.html",(context))

@login_required
def listBerita(request):
    if berita.objects.all().exists():
        instance = berita.objects.all()
    else:
        instance = None
    context={
        'username':request.session['nama'],
        'fakultas':request.session['fakultas'],
        'instance':instance
    }
    kunci = request.GET.get('kunci')
    if kunci:
        queryset_list=instance.filter(Q(judul__icontains=kunci)|Q(content__icontains=kunci)).distinct()
        context['instance']=queryset_list
    return render(request,"dash/dash_berita.html",(context))

@login_required
def timeline(request):
    context={
        'username':request.session['nama'],
        'fakultas':request.session['fakultas'],
    }
    return render(request,"dash/dash_timeline.html",(context))

@login_required
def profile(request):
    akun = request.user
    data = data_member.objects.filter(akun=akun)
    form = isi_data_member(request.POST or None, request.FILES or None)
    if data :
        data = data_member.objects.get(akun=akun)
        form = None
        context = {
        'status':True,
        'form':form,
        'user':data,
        'akun':akun,
        }
    else:
        if form.is_valid():
            instance = form.save(commit=False)
            instance.akun = request.user
            instance.daftar = True
            instance.tgl_daftar = timezone.now().date()
            instance.save()

        context = {
            "form" : form,
            'akun':akun,
        }
    context['username']=request.session['nama']
    context['fakultas']=request.session['fakultas']
    return render(request,"dash/dash_profile.html",(context))

@login_required
def pesan(request):
    akun  = request.user
    if akun.is_superuser and akun.is_staff:
        return redirect('dashboard:adm_pesan')

    listPesan = pesan_admin.objects.all()
    form=form_pesan_user(request.POST or None)
    context = {
        'formPesan':form,
        'listPesan':listPesan,
    }
    if form.is_valid():
        instance = form.save(commit=False)
        instance.pengirim = request.user
        instance.save()
        return redirect('dashboard:pesan')
    return render(request,"dash/dash_pesan.html",(context))

@login_required
def faq(request):
    context={
        'username':request.session['nama'],
        'fakultas':request.session['fakultas'],
    }

    return render(request,"dash/dash_faq.html",(context))
@login_required
def pengaturan(request):
    context={
        'username':request.session['nama'],
        'fakultas':request.session['fakultas'],
    }
    return render(request,"dash/dash_pengaturan.html",(context))
