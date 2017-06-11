# -*- coding: cp1254 -*- 
gun = 1
kar = 0
gid = 0
yep = 0
yop = 0
dgr = 0
while True:
    print gun,".gun"
    kar =  int(raw_input("Karınızı yazınız:"))
    yep =  int(raw_input("Yemek paranız:"))
    yop =  int(raw_input("Yol paranız:"))
    dgr =  int(raw_input("Diger ihtiyaclariniz:"))
    print "Yemek paranız          ",yep
    print "Yol paranız            ",yop
    print "Diger ihtiyaclariniz   ",dgr
    
    print "Toplam Harcamalariniz  ",gid
    gid=yep+yop+dgr
    
    print "------------------------------"
    print"Gideriniz ------------>",gid
    print "Toplam kazancınız---->",kar-gid
    print "------------------------------"
    gun=gun+1
    if kar == 000:
        break
    if yep == 000:
        break
    if yop == 000:
        break
    if dgr == 000:
        break
    
    
