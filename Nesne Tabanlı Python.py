+#class Araba():
#    def __init__(self,model,renk,silindir,beygirgücü):
#        self.model=model
#        self.renk=renk
#        self.silindir=silindir
#        self.beygirgücü=beygirgücü
        
    
#araba1=Araba("MERCEDES BENZ","SİYAH","8","700") #Model,renk vb bilgileri tanımlarken sınıf objesindeki sıraya göre tanımlamalıyız.
#araba2=Araba("BMW","MAVİ","8","670")            #Çağırırken istediğimiz sırada çağırabiliriz.

#print(araba1.model,araba1.renk,araba1.beygirgücü,araba1.silindir)
#print(araba2.model,araba2.renk,araba2.beygirgücü,araba2.silindir)


#class Araba():
#    def __init__(self,marka="Bilgi Yok",model="Bilgi Yok",renk="Bilgi Yok",silindir="Bilgi Yok",beygirgücü="Bilgi Yok"):
#        self.model=model
#        self.renk=renk
#        self.silindir=silindir
#        self.beygirgücü=beygirgücü
#        self.marka=marka

#araba1=Araba(marka="Pagani")
#print("Marka:",araba1.marka)

#araba1=Araba(model="Huayra")
#print("Model:",araba1.model)

#araba1=Araba(beygirgücü= 900)
#print("Beygir:",araba1.beygirgücü)

#araba1=Araba(silindir=12 )
#print("Silindir:",araba1.silindir)

#araba1=Araba(renk="Kırmızı")
#print("Renk:",araba1.renk)

#print("\n")

#araba2=Araba(marka="Koenigsegg")
#print("Marka:",araba2.marka)

#araba2=Araba(model="Jesko Attack Odin")
#print("Model:",araba2.model)

#araba2=Araba(beygirgücü=1280)
#print("Beygir:",araba2.beygirgücü)

#araba2=Araba(silindir=8)
#print("Silindir:",araba2.silindir)

#araba2=Araba(renk="Siyah")
#print("Renk:",araba2.renk)


#class Yazılımcı():
#    def __init__(self,isim,soyisim,TCKN,maaş,diller):
#        self.isim=isim
#        self.soyisim=soyisim
#        self.TCKN=TCKN,
#        self.maaş=maaş
#        self.diller=diller

#    def bilgilerigoster(self):
#        print("""
     #   İsim: {}

    #    Soyisim:{}

   #     TCKN:{}

  #      Maaş:{}                  

 #       Diller:{}
#       """.format(self.isim,self.soyisim,self.TCKN,self.maaş,self.diller))

#    def dilekle(self,yeni_dil):
#        print("Dil ekleniyor...")
#        self.diller.append(yeni_dil)

#    def zamm(self):
        
#        oran=int(input("istediğiniz zam oranını yazınız "))
#        zam_miktarı=(self.maaş*oran)/100
#        self.maaş+=zam_miktarı
#        return self.maaş

#yazılımcı=Yazılımcı(isim="Batuhan",soyisim="Bodur",TCKN="123456789",maaş=90000,diller=["PYTHON","JAVA","JAVASCRİPT","C"])


#print(yazılımcı.bilgilerigoster())


#class Çalışan():
#    def __init__(self,isim,maaş,departman):
#        self.isim=isim
#        self.maaş=maaş
#        self.departman=departman

#    def bilgilerigoster(self):
#        print("İsim:{}\nMaaş:{}\nDepartman:{}".format(self.isim,self.maaş,self.departman))    

#    def departmandegis(self,yeni_departman):
#        print("Departman değiştiriliyor")
#        self.departman=yeni_departman


#class Yönetici(Çalışan):
#    pass

#yönetici=Yönetici("Batuhan",3000,"Software dev")
#print(yönetici.bilgilerigoster())
#print(yönetici.departmandegis("Web Dev"))
#print(yönetici.bilgilerigoster())




#/////////////////////////////////////////////Proje 2////////////////////////////////////////////////////////////////
#Bir tane "Bilgisayar" sınıfı oluşturarak bu sınıfa metodlar ve özellikler ekleyin ve bu class'ı kullanmaya çalışın.

#import random
#import time

#class Bilgisayar():
#    def __init__(self,pc_durum="Kapalı",pc_açkapa="X",dosya_aç="B",dosya_sil="B",dosya_ekle="B",dosya=["Kullanıcı Verileri","Sistem Dosyaları","Oyun Dosyası","İndirilenler","Resimler"],dosya_sayısı=5):
#        self.pc_durum=pc_durum
#        self.pc_aç=pc_açkapa
#        self.dosya_aç=dosya_aç
#        self.dosya_sil=dosya_sil
#        self.dosya_ekle=dosya_ekle
#        self.dosya=dosya
#        self.dosya_sayısı=dosya_sayısı

#    def bilgigoster(self):
#        dosya_listesi = ", ".join(self.dosya)  # Dosya listesini virgülle ayrılmış bir dizeye dönüştür
#        bilgi = "{}\nDosya Sayısı: {}\nDosyalar: {}".format(self.pc_durum, self.dosya_sayısı, dosya_listesi)
#        print(bilgi)


#    def pcaç(self):
#        if(self.pc_durum=="Kapalı"):
#            print("Bilgisayar Açılıyor...")
#            time.sleep(2)
#            print("Hoşgeldiniz")
#            self.pc_durum="Açık"
        
#        else:
#            print("Bilgisayar kapatılıyor...")
#            time.sleep(1)
#            self.pc_durum="Kapalı"    
        

#    def dosaç(self):
#        i=int(input("Açmak istediğiniz dosyanın indeksini girin:"))
#        self.dosya[i]
#        print(self.dosya[i])  
    
#    def dossil(self):
#        i=int(input("Silmek istediğiniz dosya indeksini giriniz:"))
#        self.dosya.pop(i)
#        print("Dosya Siliniyor...")
#        time.sleep(1)
#        self.dosya_sayısı-=1
#        print("Dosya başarıyla silindi")

#    def dosekle(self):
#        i=input("Eklemek istediiniz dosyanın ismini giriniz:")
#        self.dosya.append(i)
#        print("Dosya Ekleniyor...")
#        time.sleep(1)
#        self.dosya_sayısı+=1
#        print("yeni dosya eklendi.")


    
#kullanıcı=Bilgisayar()
#while True:
#        print("1-)PC AÇ\n2-)DOSYA AÇ\n3-)DOSYA SİL\n4-)DOSYA EKLE\n5-)PC DURUM BİLGİSİ")
#        işlem=int(input("İşlemi seçiniz:"))
#        if(işlem==1):
#            print(kullanıcı.pcaç())
            
#        elif(işlem==2):   
#            print(kullanıcı.dosaç())
           
#        elif(işlem==3):
#            print(kullanıcı.dossil())
          
#        elif(işlem==4):
#            print(kullanıcı.dosekle())
            
#        elif(işlem==5):
#            print(kullanıcı.bilgigoster())
           
#        else:
#          print("Geçersiz işlem!!")  
    


#/////////////////////////////////////////Proje 3/////////////////////////////////////////////////////
#Bu projede ise 4 tane sınıfı oluşturun.

#Hayvan Sınıfı ------> Bütün hayvanların ortak özelliklerinin toplandığı sınıf olacak.

#Köpek Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa köpeklere ait ek özellikler ve metodlar ekleyin.

#Kuş Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa kuşlara ait ek özellikler ve metodlar ekleyin.

#At Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa atlara ait ek özellikler ve metodlar ekleyin.
                                


#class Hayvan():
#    def __init__(self,hareket=" ile hareket eder",solunum=" ile solunumu gerçekleştirir.",beslenme="ile beslenir.",üreme=" yoluyla ürer."):
#        self.hareket=hareket
#        self.solunum=solunum
#        self.beslenme=beslenme
#        self.üreme=üreme
        
#class Köpek(Hayvan):
#    def __init__(self, hareket="Patileri ile hareket eder", solunum="Akciğer ile solunumu gerçekleştirir.", beslenme="Mama ve et ürünleri ile beslenir.", üreme="Doğurma yoluyla ürer.,",iletişim="Havlayarak ve koklayarak ietişim kurar."):
#        super().__init__(hareket, solunum, beslenme, üreme)
#        self.iletişim=iletişim

#    def iletişim(self):
#        print(self.iletişim)    


#    def hareket(self):
#        print(self.hareket)

#    def solunum(self):
#        print(self.solunum) 

#    def beslenme(self):
#        print(self.beslenme)

#    def üreme(self):
#        print(self.üreme)



#class Kuş(Hayvan):
#    def __init__(self, hareket="Uçarak ve gerektiğinde ayakları ile yürüyerek hareket eder", solunum="Akciğer ile solunumu gerçekleştirir.", beslenme="Tahıl ve böceklerle beslenir.", üreme="Yumurtlama yoluyla ürer.",deri="Derilerini kaplayan tüyler sayesinde hem ıslanmaktan korunur hem de tüylerin hafif ve aerodinamik yapısı sayesinde uçma yeteneği kazanırlar.",kanat="Diğer hayvanlardan ayıran en büyük özelliği kanatlara sahip olmasıdır.Bu sayede uçabilirler."):
#        super().__init__(hareket, solunum, beslenme, üreme)
#        self.kanat=kanat
#        self.deri=deri

#    def hareket(self):
#        print(self.hareket)

#    def solunum(self):
#        print(self.solunum) 

#    def beslenme(self):
#        print(self.beslenme)

#    def üreme(self):
#        print(self.üreme)

#    def deri(self):
#        print(self.deri)

#    def kanat(self):
#        print(self.kanat)



#class At(Hayvan):
#    def __init__(self, hareket="Toynakları ile hareket eder", solunum="Akciğer ile solunumu gerçekleştirir.", beslenme="Kuru ve yaş otlar ile beslenir.", üreme="Doğurma yoluyla ürer.",dayanıklılık="Diğer hayvanlara göre daha uzun süre ayakta kalabilirler.",güç="Diğer hayvanlarla arasında bariz bir güç farkı vardır.Öyle ki bir at tonlarca yükü taşıyabilir."):
#        super().__init__(hareket, solunum, beslenme, üreme)            
    
#        self.güç=güç
#        self.dayanıklılık=dayanıklılık
        
#    def hareket(self):
#        print(self.hareket)

#    def solunum(self):
#        print(self.solunum) 

#    def beslenme(self):
#        print(self.beslenme)

#    def üreme(self):
#        print(self.üreme)

#    def dayanıklılık(self):
#        print(self.dayanıklılık)

#    def güç(self):
#        print(self.güç)


#kuş=Kuş()
#print(kuş.deri)

