from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse, Http404,HttpRequest
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import isi_data_member,isi_data_admin
from .models import data_member,data_admin,hasil_kalkulasi
from django.utils import timezone
from django import template
import datetime
from django.db import connection
from django.contrib.gis.geoip2 import GeoIP2


@login_required
def dashboard_home(request):
    kota = GeoIP2().city('36.73.70.173')
    kotaa = request.META.get('REMOTE_ADDR')
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
def berita(request):
    context={
        'username':request.session['nama'],
        'fakultas':request.session['fakultas'],
    }
    return render(request,"dash/dash_berita.html",(context))

@login_required
def timeline(request):
    context={
        'username':request.session['nama'],
        'fakultas':request.session['fakultas'],
    }
    return render(request,"dash/dash_timeline.html",(context))

@login_required
def pengumuman(request):
    if hasil_kalkulasi.objects.all().exists():
        instance = hasil_kalkulasi.objects.all()
    else:
        instance = None
    context={
        'username':request.session['nama'],
        'fakultas':request.session['fakultas'],
        'instance':instance,
    }

    return render(request,"dash/dash_pengumuman.html",(context))

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
def pengaturan(request):
    context={
        'username':request.session['nama'],
        'fakultas':request.session['fakultas'],
    }
    return render(request,"dash/dash_pengaturan.html",(context))

@login_required
def adm_berita(request):
    context={}
    return render(request,"dash/adm_berita.html",(context))

@login_required
def adm_profile(request):
    akun = request.user
    dataAdmin = data_admin.objects.filter(akun=akun)
    if dataAdmin:
        akun=request.user
        data = data_admin.objects.get(akun=akun)
        form =None
        context ={
            'status':True,
            'form':form,
            'dataUser':data,
            'akun':akun,
        }

    context['username']=request.session['nama']
    context['fakultas']=request.session['fakultas']
    return render(request,"adm/adm_profile.html",(context))

@login_required
def adm_profile_detail(request,id=id):
    instance = get_object_or_404(data_member,id=id)
    namaPanggilan = instance.nama.split()
    namaPanggilan = namaPanggilan[0]
    context = {
        "namaPanggilan":namaPanggilan,
        "nama": instance.nama,
        "instance":instance,
        'username':request.session['nama'],
        'fakultas':request.session['fakultas'],
    }
    return render(request, "adm/profile_detail.html",context)



@login_required
def adm_listPendaftar(request):
    queryset = data_member.objects.all()
    context={
        "object_list":queryset,
        "title":"List Pendaftar",
        'username':request.session['nama'],
        'fakultas':request.session['fakultas'],
    }
    return render(request,"adm/adm_listPendaftar.html",(context))
