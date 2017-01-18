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

from processors.fuzzify import fuzzifyIPK,fuzzifyORG,fuzzifyPOT,fuzzifyPRE,fuzzifyTAN
from processors.rules import rulesMin

@login_required
def adm_berita(request):
    akun = request.user
    if not akun.is_superuser and not akun.is_staff:
        return redirect('dashboard:berita')

    form = form_berita(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.author = request.user
        instance.save()
        return redirect('dashboard:adm_berita')
    context={
        'formBerita' : form,
    }

    return render(request,"adm/adm_berita.html",(context))

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

    return render(request,"adm/adm_pengumuman.html",(context))

@login_required
def adm_profile(request):
    akun = request.user
    dataAdmin = data_admin.objects.filter(akun=akun)
    form = isi_data_admin(request.POST or None, request.FILES or None)
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
    else:
        if form.is_valid():
            instance = form.save(commit=False)
            instance.akun = request.user
            instance.daftar = True
            instance.tgl_daftar = timezone.now().date()
            instance.save()
        context ={
            'form':form,

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
def adm_pesan(request):
    akun  = request.user
    if not akun.is_superuser and not akun.is_staff:
        return redirect('dashboard:pesan')

    listPesan = pesan_user.objects.all()
    form=form_pesan_admin(request.POST or None)
    context = {
        'formPesan':form,
        'listPesan':listPesan,
    }
    if form.is_valid():
        instance = form.save(commit=False)
        instance.pengirim = request.user
        instance.save()
        return redirect('dashboard:adm_pesan')
    return render(request,"dash/dash_pesan.html",(context))




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


@login_required
def validasi_pendaftar(request,id=id):
    if request.user.is_superuser:
        instance = get_object_or_404(data_member,id=id)
        cursor = connection.cursor()
        akun = instance.id
        nama = instance.nama
        fakultas = instance.fakultas
        prodi = instance.prodi
        diterima = False
        nim=instance.nim
        ipk = instance.ipk
        tan = instance.tan
        pot = instance.pot
        pre = instance.pre
        org = instance.org
        listIPK = []
        listTAN = []
        listPOT = []
        listPRE = []
        listORG = []
        for i in fuzzifyIPK(ipk):
            listIPK.append(i)
        for i in fuzzifyTAN(tan):
            listTAN.append(i)
        for i in fuzzifyPOT(pot):
            listPOT.append(i)
        for i in fuzzifyPRE(pre):
            listPRE.append(i)
        for i in fuzzifyORG(org):
            listORG.append(i)
        rekomendasi = rulesMin(listIPK, listTAN, listPOT, listPRE, listORG)
        hasil = [akun,nama,nim,fakultas,prodi,tan,pot,pre,org,ipk,rekomendasi,diterima]
        sql="INSERT INTO dashboard_hasil_kalkulasi (akun,nama,nim,fakultas,prodi,tan,pot,pre,org,ipk,rek,diterima) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, hasil)
        connection.commit()
        connection.close()
        instance.valid=True
        instance.save()
    else:
        raise Http404
    return redirect('dashboard:listPendaftar')

def terima(request,id=id):
    if request.user.is_superuser:

        instance = get_object_or_404(hasil_kalkulasi,akun=id)
        instance.diterima=True
        instance.save()
    else:
        raise Http404
    return redirect('dashboard:pengumuman')
