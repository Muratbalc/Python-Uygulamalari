# -*- coding: cp1254 -*-  #Windows için Türkçe karakter dil kodlamasını belli ettik

print "Benim ismim Sefas " 
print "Merhaba İsmini öğrenebilirmiyim ?"
isim = raw_input("İsmin nedir: ")
print "Demek ismin",isim,"'hımm...."
print "Tanıştığımıza Memnun oldum",isim
cevap = raw_input("eee nasılsın"+isim+" (Evet iyiyim[e]/Hayır iyi değilim [h])")
cevap2 = "" #if koşulluna doğrudan cevap2 = raw_input("sadas") yazsaydık hata verecekti bizde ilk olarak cevap2'yi burada belirttik
if cevap == "e":   
                print "Bunu duyduğum iyi oldu :D"
if cevap == "h":
                cevap2=raw_input("Bu kötü başından olay mı geçti ?(e/h)")
if cevap2 == "e": 
                print "Anlat Dinliyorum"
                raw_input("")
                print "Neyse bu kötü olmuş",isim,"ben gidiyorum kendine iyi bak"
if cevap2 == "h":
                print "Peki seni üzen nedir ?"
                raw_input("")
                print "Neyse bu kötü olmuş ben gidiyorum kendine iyi bak"
                
