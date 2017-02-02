from django.shortcuts import render,get_object_or_404,redirect
from reportlab.pdfgen import canvas

from django.http import HttpResponse, Http404,HttpRequest
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import isi_data_member,isi_data_admin,form_berita,form_pesan_admin,form_pesan_user,form_timeline_penerimaan,form_timeline_pengumuman,form_timeline_seleksi,form_timeline_review,form_timeline_pendaftaran,form_faq
from .models import data_member,data_admin,hasil_kalkulasi,berita,pesan_admin,pesan_user,timeline,faq
from django.utils import timezone
from django import template
import datetime
from django.db import connection
from django.db.models import Q
from django.contrib.gis.geoip2 import GeoIP2

from processors.fuzzify import fuzzifyIPK,fuzzifyORG,fuzzifyPOT,fuzzifyPRE,fuzzifyTAN
from processors.rules import rulesMin

import reportlab
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors


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
        instance = hasil_kalkulasi.objects.all().order_by("-rek")
    else:
        instance = None
    context={
        'username':request.session['nama'],
        'fakultas':request.session['fakultas'],
        'ava_url':request.session['ava_url'],
        'instance':instance,
    }
    if request.method == 'POST':
        prodi = request.POST['prodi']
        fakultas = request.POST['fakultas']
        filter_fakultas = hasil_kalkulasi.objects.filter(fakultas=fakultas, prodi=prodi).order_by("-rek")
        # context['filter_fakultas'] = filter_fakultas
        # context['prodi'] = prodi
        # context['fakultas'] = fakultas
        context['instance']=filter_fakultas
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
    context['ava_url']=request.session['ava_url']
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
    context['username']=request.session['nama']
    context['fakultas']=request.session['fakultas']
    context['ava_url']=request.session['ava_url']
    return render(request, "adm/profile_detail.html",context)

@login_required
def adm_pesan(request):
    akun  = request.user
    if not akun.is_superuser and not akun.is_staff:
        return redirect('dashboard:pesan')

    instance = pesan_user.objects.all()
    form=form_pesan_admin(request.POST or None)
    context = {
        'formPesan':form,
        'instance':instance,
    }
    if form.is_valid():
        instance = form.save(commit=False)
        instance.pengirim = request.user
        instance.save()
        return redirect('dashboard:adm_pesan')
    kunci = request.GET.get('kunci')
    if kunci:
        # akunPengirim=User.objects.get(akun=kunci)
        queryset_list=instance.filter(Q(content__icontains=kunci)|Q(subjek__icontains=kunci)).distinct()
        context['instance']=queryset_list
    context['username']=request.session['nama']
    context['fakultas']=request.session['fakultas']
    context['ava_url']=request.session['ava_url']
    return render(request,"adm/adm_pesan.html",(context))




@login_required
def adm_listPendaftar(request):
    instance = data_member.objects.all().order_by('-valid')
    context={
        "instance":instance,
        "title":"List Pendaftar",
        'username':request.session['nama'],
        'fakultas':request.session['fakultas'],
        'nomor':1,
    }
    kunci = request.GET.get('kunci')
    if kunci:
        queryset_list=instance.filter(Q(nama__icontains=kunci)).distinct()
        context['instance']=queryset_list
    context['username']=request.session['nama']
    context['fakultas']=request.session['fakultas']
    context['ava_url']=request.session['ava_url']
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
        tunggu,diterima =True, False
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
        hasil = [akun,nama,nim,fakultas,prodi,tan,pot,pre,org,ipk,rekomendasi,tunggu,diterima]
        sql="INSERT INTO dashboard_hasil_kalkulasi (akun,nama,nim,fakultas,prodi,tan,pot,pre,org,ipk,rek,tunggu,diterima) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, hasil)
        connection.commit()
        connection.close()
        instance.valid=True
        instance.save()
    else:
        raise Http404
    return redirect('dashboard:listPendaftar')

def terima_pendaftar(request,id=id):
    if request.user.is_superuser:

        instance = get_object_or_404(hasil_kalkulasi,akun=id)
        instance.diterima=True
        instance.tunggu =False
        instance.save()
    else:
        raise Http404
    return redirect('dashboard:adm_pengumuman')

def tolak_pendaftar(request,id=id):
    if request.user.is_superuser:

        instance = get_object_or_404(hasil_kalkulasi,akun=id)
        instance.diterima=False
        instance.tunggu =False
        instance.save()
    else:
        raise Http404
    return redirect('dashboard:adm_pengumuman')

def cetakTest(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)
    nama = request.user.username
    email = request.user.email
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world. %s %s" % (nama,email))

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response

def del_faq(request,id=id):
    if not request.user.is_superuser:
        return redirect('dashboard:faq')
    instance = faq.objects.get(id=id)
    instance.delete()
    return redirect('dashboard:faq')

def edit_faq(request,id=id):
    if not request.user.is_superuser:
        return redirect('dashboard:faq')
    instance = faq.objects.get(id=id)
    form = form_faq(request.POST or None,instance=instance)
    context = {
        'form':form,
    }
    if form.is_valid():
        i = form.save(commit=False)
        i.save()
        return redirect('dashboard:faq')
    return render(request,'adm/edit_faq.html',(context))

def del_berita(request,id=id):
    if not request.user.is_superuser:
        return redirect('dashboard:berita')
    instance = berita.objects.get(id=id)
    instance.delete()
    return redirect('dashboard:berita')

def edit_berita(request,id=id):
    if not request.user.is_superuser:
        return redirect('dashboard:berita')
    instance = berita.objects.get(id=id)
    form = form_berita(request.POST or None,instance=instance)
    context = {
        'form':form,
    }
    if form.is_valid():
        i = form.save(commit=False)
        i.save()
        return redirect('dashboard:berita')
    return render(request,'adm/edit_berita.html',(context))

def cetak_rekap_pendaftar(request):
    # pengaturan respon berformat pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="rekapan_pendaftar.pdf"'

    # mengambil daftar kehadiran dan mengubahnya menjadi data ntuk tabel
    data = data_member.objects.all()
    table_data = []
    table_data.append([ "Nama","NIM","Fakultas","Prodi" ])
    for x in data:
        table_data.append([ x.nama, x.nim, x.fakultas, x.prodi ])


    # membuat dokumen baru
    doc = SimpleDocTemplate(response, pagesize=A4, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)
    styles = getSampleStyleSheet()

    # pengaturan tabel di pdf
    table_style = TableStyle([
                               ('ALIGN',(1,1),(-2,-2),'LEFT'),
                               ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold'),
                               ('VALIGN',(0,0),(0,-1),'TOP'),
                               ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                               ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                           ])
    pendaftar_table = Table(table_data, colWidths=[doc.width/4.0]*2)
    pendaftar_table.setStyle(table_style)

    # mengisi pdf
    content = []
    content.append(Paragraph('Daftar Rekapan Mahasiswa Pendaftar Beasiswa Astra', styles['Title']))
    content.append(Spacer(1,12))
    content.append(Paragraph('Berikut ini adalah rekapannya' , styles['BodyText']))
    content.append(Spacer(1,12))
    content.append(pendaftar_table)
    content.append(Spacer(1,36))
    content.append(Paragraph('Mengetahui, ', styles['Normal']))
    content.append(Spacer(1,48))
    content.append(Paragraph('Wakil Dekan III ', styles['Normal']))

    # menghasilkan pdf untk di download
    doc.build(content)
    return response

def cetak_rekap_diterima(request):
    # pengaturan respon berformat pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="penerima.pdf"'

    # mengambil daftar kehadiran dan mengubahnya menjadi data ntuk tabel
    data = hasil_kalkulasi.objects.filter(diterima=True)
    table_data = []
    table_data.append([ "Nama", "NIM","Fakultas","Prodi" ])
    for x in data:
        table_data.append([ x.nama, x.nim,x.fakultas,x.prodi ])


    # membuat dokumen baru
    doc = SimpleDocTemplate(response, pagesize=A4, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)
    styles = getSampleStyleSheet()

    # pengaturan tabel di pdf
    table_style = TableStyle([
                               ('ALIGN',(1,1),(-2,-2),'RIGHT'),
                               ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold'),
                               ('VALIGN',(0,0),(0,-1),'TOP'),
                               ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                               ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                           ])
    kehadiran_table = Table(table_data, colWidths=[doc.width/4.0]*2)
    kehadiran_table.setStyle(table_style)

    # mengisi pdf
    content = []
    content.append(Paragraph('Daftar Penerima Beasiswa Astra' , styles['Title']))
    content.append(Spacer(1,12))
    content.append(Paragraph('Berikut adalah daftar mahasiswa :' , styles['Normal']))
    content.append(Spacer(1,12))
    content.append(kehadiran_table)
    content.append(Spacer(1,36))
    content.append(Paragraph('Mengetahui, ', styles['Normal']))
    content.append(Spacer(1,48))
    content.append(Paragraph('Wakil Dekan III,', styles['Normal']))

    # menghasilkan pdf untk di download
    doc.build(content)
    return response

def cetak_rekapan_ditolak(request):
    # pengaturan respon berformat pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="daftar_ditolak.pdf"'

    # mengambil daftar kehadiran dan mengubahnya menjadi data ntuk tabel
    data = hasil_kalkulasi.objects.filter(diterima=False)
    table_data = []
    table_data.append([ "Nama", "NIM", "Fakultas", "Prodi" ])
    for x in data:
        table_data.append([ x.nama, x.nim,x.fakultas,x.prodi ])


    # membuat dokumen baru
    doc = SimpleDocTemplate(response, pagesize=A4, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)
    styles = getSampleStyleSheet()

    # pengaturan tabel di pdf
    table_style = TableStyle([
                               ('ALIGN',(1,1),(-2,-2),'RIGHT'),
                               ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold'),
                               ('VALIGN',(0,0),(0,-1),'TOP'),
                               ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                               ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                           ])
    kehadiran_table = Table(table_data, colWidths=[doc.width/4.0]*2)
    kehadiran_table.setStyle(table_style)

    # mengisi pdf
    content = []
    content.append(Paragraph('Daftar Mahasiswa yang tidak lolos', styles['Title']))
    content.append(Spacer(1,12))
    content.append(Paragraph('Berikut ini adalah hasilnya :' , styles['Normal']))
    content.append(Spacer(1,12))
    content.append(kehadiran_table)
    content.append(Spacer(1,36))
    content.append(Paragraph('Mengetahui, ', styles['Normal']))
    content.append(Spacer(1,48))
    content.append(Paragraph('Wakil Dekan III, ', styles['Normal']))

    # menghasilkan pdf untk di download
    doc.build(content)
    return response

def cetak_rekapan_sorting(request,tahun,prodi,fakultas):
    # pengaturan respon berformat pdf
    filename = "rekapan_"+ str(fakultas) +"_"+str(tahun)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=' + filename + '.pdf'

    # mengambil daftar kehadiran dan mengubahnya menjadi data ntuk tabel
    data = tb_akun_member.objects.filter(tgl_daftar__year=tahun,prodi=prodi,fakultas=fakultas)
    table_data = []
    table_data.append([ "Nama", "NIM","Fakultas","Prodi" ])
    for x in data:
        table_data.append([ x.nama, x.nim,x.fakultas,x.prodi ])


    # membuat dokumen baru
    doc = SimpleDocTemplate(response, pagesize=A4, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)
    styles = getSampleStyleSheet()

    # pengaturan tabel di pdf
    table_style = TableStyle([
                               ('ALIGN',(1,1),(-2,-2),'LEFT'),
                               ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold'),
                               ('VALIGN',(0,0),(0,-1),'TOP'),
                               ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                               ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                           ])
    sorting_table = Table(table_data, colWidths=[doc.width/4.0]*2)
    sorting_table.setStyle(table_style)

    # mengisi pdf
    content = []
    content.append(Paragraph('Daftar Rekapan Mahasiswa Pendaftar Beasiswa Astra', styles['Title']))
    content.append(Spacer(1,12))
    content.append(Paragraph('Berikut ini adalah rekapannya berdasarkan /%s/%s/%s'%(fakultas,prodi,tahun) , styles['BodyText']))
    content.append(Spacer(1,12))
    content.append(sorting_table)
    content.append(Spacer(1,36))
    content.append(Paragraph('Mengetahui, ', styles['Normal']))
    content.append(Spacer(1,48))
    content.append(Paragraph('Wakil Dekan III ', styles['Normal']))

    # menghasilkan pdf untk di download
    doc.build(content)
    return response

def del_hasil_kalkulasi(request):
    hasil_kalkulasi.objects.all().delete()
    return redirect("dashboard:adm_pengumuman")

def invalidasi_pendaftar(request,id=id):
    instance = get_object_or_404(data_member,id=id)
    instance.valid = False
    instance.save()
    return redirect("dashboard:listPendaftar")
