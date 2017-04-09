# -*- coding: cp1254 -*-  #Windows için Türkçe karakter dil kodlamasını belli ettik

from __future__ import division  #x sayısından sonra gelecek virgüllü sayıları belirttik

#seçenek sunduk

secenek1 = "(1) toplama"
secenek2 = "(2) çıkarma"
secenek3 = "(3) çarpma"
secenek4 = "(4) bölme"

#seçenekler,programın ismi ve kaynağı ekrana çıktısını yazdırdık

print "Python Hesap Makinesi"
print "P.H.M"
print "Kaynak:İstihza"
print secenek1
print secenek2
print secenek3
print secenek4

#Kullanıcıdan bilgi aldık

soru = raw_input("Yapılacak işlemin numarasını girin: ")

#Toplama işlemi

if soru == "1":
                sayi1 = int(raw_input("Toplama için ilk sayıyı girin: "))
                print sayi1
                sayi2 = int(raw_input("Toplama için ikinci sayıyı girin: "))
                print sayi1, "+", sayi2, ":" , sayi1+sayi2
#Çıkarma işlemi
                
if soru == "2":
                sayi1 = int(raw_input("Çıkarma için ilk sayıyı girin: "))
                print sayi1
                sayi2 = int(raw_input("Çıkarma için ikinci sayıyı girin: "))
                print sayi1, "-", sayi2, ":" , sayi1-sayi2
#Çarpma İşlemi
                
if soru == "3":
                sayi1 = int(raw_input("Çarpma ilk sayıyı girin: "))
                print sayi1
                sayi2 = int(raw_input("Çarpma için ikinci sayıyı girin: "))
                print sayi1, "*", sayi2, ":" , sayi1*sayi2
#Bölme İşlemi
                
if soru == "4":
                sayi1 = int(raw_input("Bölme için ilk sayıyı girin: "))
                print sayi1
                sayi2 = int(raw_input("Bölme için ikinci sayıyı girin: "))
                print sayi1, "/", sayi2, ":" , sayi1/sayi2
                
                
