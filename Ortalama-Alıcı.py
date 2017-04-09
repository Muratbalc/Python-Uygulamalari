# -*- coding: cp1254 -*-  #Windows için Türkçe karakter dil kodlamasını belli ettik

from __future__ import division

ders1 ="[1] Türkçe"
ders2 ="[2] Matematik"
ders3 ="[3] Fen Bilgisi"
ders4 ="[4] İnkılap"
ders5 ="[5] İngilizce"

print ders1
print ders2
print ders3
print ders4
print ders5

ders = int(raw_input("Ders Seçin (1-5):"))

if ders == 1:
                nb = int(raw_input("İlk Ders Notu:"))
                ni = int(raw_input("İkinci ders Notu: "))
                nu = int(raw_input("Üçüncü Ders Notu:"))
                no=nb+ni+nu 
                print "Ortalamanız:",no/3
if ders == 2:
                nb = int(raw_input("İlk Ders Notu:"))
                ni = int(raw_input("İkinci ders Notu: "))
                nu = int(raw_input("Üçüncü Ders Notu:"))
                no=nb+ni+nu 
                print "Ortalamanız:", no/3
if ders == 3:
                nb = int(raw_input("İlk Ders Notu:"))
                ni = int(raw_input("İkinci ders Notu: "))
                nu = int(raw_input("Üçüncü Ders Notu:"))
                no=nb+ni+nu 
                print "Ortalamanız:", no/3
if ders == 4:
                nb = int(raw_input("İlk Ders Notu:"))
                ni = int(raw_input("İkinci ders Notu: "))
                no=nb+ni
                print "Ortalamanız:", no/2
if ders == 5:
                nb = int(raw_input("İlk Ders Notu:"))
                ni = int(raw_input("İkinci ders Notu: "))
                nu = int(raw_input("Üçüncü Ders Notu:"))
                no=nb+ni+nu 
                print "Ortalamanız:", no/3
if ders > 5:
                print "Ders Seçmediniz Lütfen Ders Seçin !!!(Uygulama Kapanacaktır)"
if ders < 1:
                print "Ders Seçmediniz Lütfen Ders Seçin !!!(Uygulama Kapanacaktır)"
