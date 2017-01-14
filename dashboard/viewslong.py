from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse, Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import isi_data_member,isi_data_admin
from .models import data_member,data_admin,hasil_kalkulasi
from django.utils import timezone
from django import template
import datetime
from django.db import connection
from processors.fuzzify import fuzzifyIPK,fuzzifyORG,fuzzifyPOT,fuzzifyPRE,fuzzifyTAN
from processors.rules import rulesMin

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
