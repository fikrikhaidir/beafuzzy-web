def fuzzifyIPK(ipk):
    rendah = 0
    sedang = 0
    tinggi = 0
    a1,b1 ,c1 = 2.7 , 2.9, 3.22
    a2,b2 ,c2 = 3.11 , 3.32, 3.54
    a3,b3 ,c3 = 3.43, 3.71, 4.0
    MuSedang = 0
    MuRendah = 0
    MuTinggi = 0

    ipk = float(ipk)#Convert masukan menjadi float

    if (ipk <= c1): #Barrier pertama, untuk keanggotaan "Rendah"

        if (ipk<b1):
            MuRendah = 1

        elif(ipk>=b1 and ipk<c1):
            temp1 = c1-ipk
            temp2 = c1-b1
            MuRendah = temp1/temp2

        else:
            MuRendah = 0


    if (ipk >= a2 and ipk <=c2):       #Barrier kedua, untuk keanggotaan "Sedang"

        if (ipk>=a2 and ipk< b2):
            temp1 = ipk-a2
            temp2 = b2-a2
            MuSedang = temp1/temp2

        elif(ipk==b2) :
            MuSedang = 1

        elif(ipk>=b2 and ipk < c2):
            temp1 = c2-ipk
            temp2 = c2-b2
            MuSedang = temp1/temp2

        else:
            MuSedang = 0

    if (ipk >= a3):     #Barrier Ketiga, untuk keanggotaan "Tinggi"

        if (ipk>=a3 and ipk < b3):
            temp1 = ipk-a3
            temp2 = b3-a3
            MuTinggi = temp1/temp2

        elif (ipk>=b3):
            MuTinggi = 1

        else:
            MuTinggi = 0

    MuRendah = float(("%.2f" % MuRendah))
    MuSedang = float(("%.2f" % MuSedang))
    MuTinggi = float(("%.2f" % MuTinggi))

    return MuRendah, MuSedang, MuTinggi  #Output Modul, nilai belum bisa di pass.

                        #Testing di baris ini.
#print MuSedang, MuRendah,MuTinggi



def fuzzifyTAN(tan):
    a1,b1 ,c1 = 0, 2, 3.4 #untuk tantasi rendah dari tingkat prodi dan fakultas
    a2,b2 ,c2 = 2.6 ,3.5 ,4.8 #untuk tantasi sedang dari tingkat universitas
    a3,b3 ,c3 = 4.5, 5, 6 #untuk tingkat nasional dan internasional
    MuSedang = 0
    MuRendah = 0
    MuTinggi = 0

    tan = float(tan)                    #Convert masukan menjadi float

    if (tan<= c1):        #Barrier pertama, untuk keanggotaan "Rendah"

        if (tan<=b1):
            MuRendah = 1

        elif(tan>b1 and tan<=c1):
            temp1 = c1-tan
            temp2 = c1-b1
            MuRendah = temp1/temp2

        else:
            MuRendah = 0


    if (tan> a2 and tan <=c2):       #Barrier kedua, untuk keanggotaan "Sedang"

        if (tan>=a2 and tan< b2):
            temp1 = tan-a2
            temp2 = b2-a2
            MuSedang = temp1/temp2

        elif(tan==b2) :
            MuSedang = 1

        elif(tan>=b2 and tan < c2):
            temp1 = c2-tan
            temp2 = c2-b2
            MuSedang = temp1/temp2

        else:
            MuSedang = 0

    if (tan >= a3):

        if (tan>=a3 and tan <b3):
            temp1 = tan-a3
            temp2 = b3-a3
            MuTinggi = temp1/temp2

        elif (tan>=b3):
            MuTinggi = 1

        else:
            MuTinggi = 0

    MuRendah = float(("%.2f" % MuRendah))
    MuSedang = float(("%.2f" % MuSedang))
    MuTinggi = float(("%.2f" % MuTinggi))

    return MuRendah, MuSedang, MuTinggi   #Output Modul, nilai belum bisa di pass.


                      #Testing di baris ini.
#print MuSedang, MuRendah,MuTinggi


def fuzzifyPOT(pot):
    rendah = 0
    sedang = 0
    tinggi = 0
    a1,b1 ,c1 = 500000,1830000, 3666666
    a2,b2 ,c2 = 2745000,4570000 , 6411000
    a3,b3 ,c3 = 5490000, 7320000, 9111000
    MuSedang = 0
    MuRendah = 0
    MuTinggi = 0

    pot = float(pot)         #Convert masukan menjadi float

    if(pot >= a3):  #Barrier kedua, untuk keanggotaan "Rendah"

       if (pot>= b3):
           MuRendah = 1

       elif (pot>=a3 and pot <= b3):
           temp1 = pot-a3
           temp2 = b3-a3
           MuRendah = temp1/temp2

       else:
           MuRendah = 0

    if (pot >= a2 and pot <=c2):       #Barrier kedua, untuk keanggotaan "Sedang"

        if (pot>=a2 and pot<= b2):
            temp1 = pot-a2
            temp2 = b2-a2
            MuSedang = temp1/temp2

        elif(pot==b2) :
            MuSedang = 1

        elif(pot>=b2 and pot <=c2):
            temp1 = c2-pot
            temp2 = c2-b2
            MuSedang = temp1/temp2

        else:
            MuSedang = 0

    if (pot <= c1  ):     #Barrier Ketiga, untuk keanggotaan "Tinggi"

        if (pot< b1):
            MuTinggi = 1

        elif (pot>=b1 and pot <= c1):
            temp1 = c1-pot
            temp2 = c1-b1
            MuTinggi = temp1/temp2

        else:
            MuTinggi = 0

    MuRendah = float(("%.2f" % MuRendah))
    MuSedang = float(("%.2f" % MuSedang))
    MuTinggi = float(("%.2f" % MuTinggi))

    return MuRendah, MuSedang, MuTinggi   #Output Modul, nilai belum bisa di pass.



#Testing di baris ini.
#print MuSedang, MuRendah,MuTinggi

def fuzzifyPRE(pre):
    rendah = 0
    sedang = 0
    tinggi = 0
    a1,b1 ,c1 = -0.6, 1.0, 2.6 #untuk prestasi rendah dari tingkat prodi dan fakultas
    a2,b2 ,c2 = 1.4 ,3.0 , 4.6 #untuk prestasi sedang dari tingkat universitas
    a3,b3 ,c3 = 3.4, 5.0, 6.6 #untuk tingkat nasional dan internasional
    MuSedang = 0
    MuRendah = 0
    MuTinggi = 0

    pre = float(pre)                    #Convert masukan menjadi float

    if (pre<=c1):        #Barrier pertama, untuk keanggotaan "Rendah"

        if (pre<b1):
            MuRendah = 1

        elif(pre>=b1 and pre<c1):
            temp1 = c1-pre
            temp2 = c1-b1
            MuRendah = temp1/temp2

        else:
            MuRendah = 0


    if (pre >= a2 and pre <=c2):       #Barrier kedua, untuk keanggotaan "Sedang"

        if (pre>=a2 and pre< b2):
            temp1 = pre-a2
            temp2 = b2-a2
            MuSedang = temp1/temp2

        elif(pre==b2) :
            MuSedang = 1

        elif(pre>=b2 and pre < c2):
            temp1 = c2-pre
            temp2 = c2-b2
            MuSedang = temp1/temp2

        else:
            MuSedang = 0

    if (pre >= a3):     #Barrier Ketiga, untuk keanggotaan "Tinggi"

        if (pre>=a3 and pre < b3):
            temp1 = pre-a3
            temp2 = b3-a3
            MuTinggi = temp1/temp2

        elif (pre>=b3):
            MuTinggi = 1

        else:
            MuTinggi = 0

    MuRendah = float(("%.2f" % MuRendah))
    MuSedang = float(("%.2f" % MuSedang))
    MuTinggi = float(("%.2f" % MuTinggi))

    return MuRendah, MuSedang, MuTinggi   #Output Modul, nilai belum bisa di pass.


def fuzzifyORG(org):
    rendah = 0
    sedang = 0
    tinggi = 0
    a1,b1 ,c1 = -0.6 , 1.1, 2.6 #untuk rendah orgnisasi prodi dan fakultas
    a2,b2 ,c2 = 1.4 , 3.0, 4.6 #untuk sedang orgnisasi universitas
    a3,b3 ,c3 = 3.4, 5, 6.6 #untuk tinggi orgnisasi nasional dan internasional
    MuSedang = 0
    MuRendah = 0
    MuTinggi = 0

    org = float(org)                    #Convert masukan menjadi float

    if (org<= c1):        #Barrier pertama, untuk keanggotaan "Rendah"

        if (org<b1):
            MuRendah = 1

        elif(org>=b1 and org<c1):
            temp1 = c1-org
            temp2 = c1-b1
            MuRendah = temp1/temp2

        else:
            MuRendah = 0


    if (org >= a2 and org <=c2):       #Barrier kedua, untuk keanggotaan "Sedang"

        if (org>=a2 and org< b2):
            temp1 = org-a2
            temp2 = b2-a2
            MuSedang = temp1/temp2

        elif(org==b2) :
            MuSedang = 1

        elif(org>=b2 and org < c2):
            temp1 = c2-org
            temp2 = c2-b2
            MuSedang = temp1/temp2

        else:
            MuSedang = 0

    if (org >= a3):     #Barrier Ketiga, untuk keanggotaan "Tinggi"

        if (org>=a3 and org < b3):
            temp1 = org-a3
            temp2 = b3-a3
            MuTinggi = temp1/temp2

        elif (org>=b3):
            MuTinggi = 1

        else:
            MuTinggi = 0

    MuRendah = float(("%.2f" % MuRendah))
    MuSedang = float(("%.2f" % MuSedang))
    MuTinggi = float(("%.2f" % MuTinggi))

    return MuRendah, MuSedang, MuTinggi   #Output Modul, nilai belum bisa di pass.


def viewFuzzified(ipk,tan,pot,pre,org):
    print "IPK : ",ipk
    print "TAN : ",tan
    print "POT : ",pot
    print "PRE : ",pre
    print "ORG : ",org
