import random
import time

class Bilgisayar():
    def __init__(self,pc_durum="Kapalı",pc_açkapa="X",dosya_aç="B",dosya_sil="B",dosya_ekle="B",dosya=["Kullanıcı Verileri","Sistem Dosyaları","Oyun Dosyası","İndirilenler","Resimler"],dosya_sayısı=5):
        self.pc_durum=pc_durum
        self.pc_aç=pc_açkapa
        self.dosya_aç=dosya_aç
        self.dosya_sil=dosya_sil
        self.dosya_ekle=dosya_ekle
        self.dosya=dosya
        self.dosya_sayısı=dosya_sayısı

    def bilgigoster(self):
        dosya_listesi = ", ".join(self.dosya)  # Dosya listesini virgülle ayrılmış bir dizeye dönüştür
        bilgi = "{}\nDosya Sayısı: {}\nDosyalar: {}".format(self.pc_durum, self.dosya_sayısı, dosya_listesi)
        print(bilgi)


    def pcaç(self):
        if(self.pc_durum=="Kapalı"):
            print("Bilgisayar Açılıyor...")
            time.sleep(2)
            print("Hoşgeldiniz")
            self.pc_durum="Açık"
        
        else:
            print("Bilgisayar kapatılıyor...")
            time.sleep(1)
            self.pc_durum="Kapalı"    
        

    def dosaç(self):
        i=int(input("Açmak istediğiniz dosyanın indeksini girin:"))
        self.dosya[i]
        print(self.dosya[i])  
    
    def dossil(self):
        i=int(input("Silmek istediğiniz dosya indeksini giriniz:"))
        if(i<=self.dosya_sayısı):
            self.dosya.pop(i)
            print("Dosya Siliniyor...")
            time.sleep(1)
            self.dosya_sayısı-=1
            print("Dosya başarıyla silindi")
        else:
            print("Geçersiz işlem!!")
            return     

    def dosekle(self):
        i=input("Eklemek istediiniz dosyanın ismini giriniz:")
        self.dosya.append(i)
        print("Dosya Ekleniyor...")
        time.sleep(1)
        self.dosya_sayısı+=1
        print("yeni dosya eklendi.")


    
kullanıcı=Bilgisayar()
while True:
        print("1-)PC AÇ\n2-)DOSYA AÇ\n3-)DOSYA SİL\n4-)DOSYA EKLE\n5-)PC DURUM BİLGİSİ")
        işlem=int(input("İşlemi seçiniz:"))
        if(işlem==1):
            print(kullanıcı.pcaç())
            
        elif(işlem==2):   
            print(kullanıcı.dosaç())
           
        elif(işlem==3):
            print(kullanıcı.dossil())
          
        elif(işlem==4):
            print(kullanıcı.dosekle())
            
        elif(işlem==5):
            print(kullanıcı.bilgigoster())
           
        else:
          print("Geçersiz işlem!!") 

