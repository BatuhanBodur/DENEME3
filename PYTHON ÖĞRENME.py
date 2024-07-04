#liste=[1,2.4,9,5,5.5,9,1,3,7,6]
#print(liste.count(5))
#print(liste.index(5))

#////////////////////////////////////////////////////////////

#print("Bu bir kök bulma poragramıdır")
#print(" ax² + bx + c şeklindeki ikinci dereceden denklemlerin kökünü bulabilirsiniz.")

#a=int(input("a:"))
#b=int(input("b:"))
#c=int(input("c:"))

#delta=(b ** 2 )- (4*(a*c))
#x1=(- b - delta ** 0.5) / ( 2 * a)
#x2=(- b + delta ** 0.5) / ( 2 * a)

#print("Birinci kök : {}\nİkinci kök : {}".format(x1,x2))

#//////////////////////////////////////////////////////////

#a=int(input("a:"))
#b=int(input("b:"))
#c=int(input("c:"))

#çarpım=a*b*c

#print("çarpım: {}*{}*{}= {} dir".format(a,b,c,çarpım))

#////////////////////////////////////////////////////////////////

#print("Beden Kitle İndeksinş bulmamız için kilo ve boy bilgilerini girin\nKilo: \nBoy:\n")
#kilo=int(input("kilo:")) 
#boy=int(input("boy:"))

#BKİ=kilo/boy

#print("Beden Kitle İndeksiniz: {}".format(BKİ))

#////////////////////////////////////////////////////////////

#print("Aracınızın kilometrede ki yakıt tüketimini giriniz")
#a=int(input())

#print("Kaç km yol yaptığınızı giriniz")
#b=int(input())

#ödeme=a*b
#print("Ödemeniz gereken tutar: {} tl ".format(ödeme))

#////////////////////////////////////////////////////////

#print("Adınızı soyadınızı ve numaranızı giriniz")
#ad=input("ad:")
#soyad=input("soyad:")
#numara=int(input("numara:"))

#print("Ad= {}\n""Soyad: {}\n""Numara: {}".format(ad,soyad,numara))

#/////////////////////////////////////////////////////////////

#print("iki sayı giriniz")
#sayi1=int(input())
#sayi2=int(input())
#sayi1,sayi2=sayi2,sayi1
#print("birinci sayi: {}\n""ikinci sayi: {}".format(sayi1,sayi2))

#///////////////////////////////////////////////////////

#print("Hipotenüs hesaplama uygulamasına hoşgeldiniz.")
#print("İlk kenarı giriniz:")
#a=int(input())
#print("İkinci kenarı giriniz:")
#b=int(input())

#hipotenüs=((a**2)+(b**2))**0.5

#print("Hiptenüs uzunluğu : {}".format(hipotenüs))

#////////////////////////////////////////////////////////

#print(bool(len("mehmet ")==len("batuhan")))

#/////////////////////////////////////////////////////////

#yaş=int(input("yaşınızı giriniz:"))
#if yaş<18:
#    print("giremezsiniz")
#else:
 #   print("hoşgeldiniz")

#/////////////////////////////////////////////////////////

#print("HESAP MAKİNASI\n1-)TOPLAMA\n2-)ÇIKARMA İŞLEMİ\n3-)ÇARPMA İŞLEMİ\n4-)BÖLME İŞLEMİ")
#işlem=(input("Yapmak istediğiniz işlemi seçiniz:"))
#a=float(input("Birinci sayi:"))
#b=float(input("İkinci sayi:"))

#if(işlem == "1"):
 #   print("{}+{}={}".format(a,b,a+b))
#elif(işlem=="2"):    
 #   print("{}-{}={}".format(a,b,a-b))
#elif(işlem=="3"):
 #   print("{}x{}={}".format(a,b,a*b))
#elif(işlem=="4"):
 #   print("{}/{}={}".format(a,b,a/b))        
#else:
 #   print("Geçersiz İşlem!")

#//////////////////////////////////////////////////////////////

#print("Beden Kitle Endeksi Hesaplayıcı\nLütfen kilo ve boy bilgilerini giriniz")
#kilo=int(input("Kilo:"))
#boy=float(input("Boy:"))

#BKİ=(kilo/boy)*boy

#if(BKİ<18.5):
 #   print("Zayıfsınız")
#elif(18.5 <= BKİ <25):
 #   print("Normalsiniz")
#elif(25<=BKİ<30):
 #   print("Fazla kilolusunuz") 
#else:
 #   print("Obezsiniz") 

#//////////////////////////////////////////////////////

#print("Karşılaştırmak istediğiniz üç sayıyı giriniz")
#a=int(input("Birinci sayı:"))
#b=int(input("İkinci sayı:"))
#c=int(input("Üçüncü sayı:"))

#if(a>b and a>c):
 #   print("Birinci sayi en büyüktür")
#elif(b>a and b>c):
 #   print("İkinci sayı en büyüktür")
#elif(c>a and c>b):
 #   print("Üçüncü sayı en büyüktür")
#elif(a==b and a==c ):
#    print("Sayılar eşittir")       

#/////////////////////////////////////////////////////////////

#print("Harf notu uygulamasına hoşgeldiniz!")

#vize1=int(input("Vize1 notunuzu giriniz:"))
#vize2=int(input("Vize2 notunuzu giriniz:"))
#final=int(input("Final notunuzu giriniz:"))

#ortalama=(vize1*30/100)+(vize2*30/100)+(final*40/100)

#if(ortalama>=90):
 #   print("AA")
#elif(ortalama>=85):
 #   print("BA")
#elif(ortalama>=80):
 #   print("BB")
#elif(ortalama>=75):
 #   print("CB")
#elif(ortalama>=70):
 #   print("CC")
#elif(ortalama>=65):
 #   print("DC")
#elif(ortalama>=60):
 #   print("DD")
#elif(ortalama>=55):
#    print("FD")
#else:
#    print("FF")   

#////////////////////////////////////////////////////////////

#şekil =  input("Hangi şeklin tipini öğrenmek istiyorsunuz?")

#if (şekil == "Dörtgen"):
#    print("Lütfen kenarları sırayla giriniz.")
#    a = int(input("Kenar-1:"))
#    b = int(input("Kenar-2:"))
#    c = int(input("Kenar-3:"))
#    d = int(input("Kenar-4:"))
    
#    if (a == b and a == c and a == d):
#        print("Kare")
#    elif (a == c and b == d):
#        print("Dikdörtgen")
#    else:
#        print("Dörtgen")
        
    
    
#elif (şekil == "Üçgen"):
    #a = int(input("Kenar-1:"))
    #b = int(input("Kenar-2:"))
    #c = int(input("Kenar-3:"))
    #if ( abs(a+b) > c and abs(a+c) > b and abs(b+c) > a):
        #if (a == b and a == c ):
       #     print("Eşkenar Üçgen...")
      #  elif ((a == b and a != c) or (a == c and a != b) or (b == c and b != a)):
     #       print("İkizkenar Üçgen....")
    #    else:
   #         print("Çeşitkenar Üçgen...")
  #  else:
 #       print("Üçgen belirtmiyor...")
        
#else:
#    print("Geçersiz Şekil...")     

#//////////////////////////////////////////////////////////////////////////

#print("z" in "python")

#print(not 4 in (1,2,3))
#////////////////////////////////////////////////////////////////

#toplam=0
#liste=[1,2,3,4,5,6]
#for eleman in liste:
#    toplam+=eleman

#    print(" Eleman: {} Toplam: {}".format(eleman,toplam))
  
#////////////////////////////////////////////////////////////////

#s="batuhan"
#for i in s:
#    print(i)

#////////////////////////////////////////////////////////////////

#liste=[1,2,3,4,5,6,7]
#for eleman in liste:
    #if ((eleman % 2)==0):
     #print(eleman)

#////////////////////////////////////////////////////////////////

#liste=[(1,2),(3,4),(5,6)]
#for(i,j) in liste:
 #   print("i: {} j: {}".format(i,j))

#////////////////////////////////////////////////////////////////

#str="abc"
#for i in str:
#    print(3* i)

#///////////////////////////////////////////////////////////////
#liste=[(1,2,3),(3,4,5),(5,6,7)]
#for (i,j,k) in liste:
#    print(i*j*k)

#//////////////////////////////////////////////////////////////

#liste=[(1,2,3),(3,4,5),(5,6,7)]
#for(i,j,k) in liste:
#    print(i,j,k)

#/////////////////////////////////////////////////////////////

#sözlük={"bir":1,"iki":2,"üç":3,"dört":4,"beş":5}
#print(sözlük.keys())
#print(sözlük.values())
#print(sözlük.items())
#for i in sözlük.values():
    #print(i)

#/////////////////////////////////////////////////////////////////////

#i=0
#while(i<=10):
#    print("i nin değeri.:",i)
#    i+=1

#///////////////////////////////////////////////////////////////

#liste=[1,2,3,4,5,6]
#index=0
#while(index<len(liste)):
#    print("İndex:  {}   Liste Elemanı: {}".format(index,liste[index]))
#    index+=1

#//////////////////////////////////////////////////////////////////

#print(*range(20,0,-1))
#print(*range(5,105,5))
#for i in range(1,11):
#    print("*"*i)

#/////////////////////////////////////////////////////////////////

#while True:  #Bu döngü içerde sonlandırılmazsa sonsuza kadar gider.    
  #  isim=input("İsim ve Soyisim bilgilerinizi giriniz.\n İsim:\n Soyisim: eğer q a basılırsa program sonlanacaktır")
   # if(isim=="Q"):
    #    print("program sonlandı")
     #   break #Şart sağlandığında alttaki hiçbir işlem gerçekleştirilmez. 
      #  print("İsim:",isim)   

#//////////////////////////////////////////////////////////////////

#for i in range(0,10):
#    if(i%2==0):
#        print(i,"Çift sayı tespit edildi")
#        continue #Şart sağlandığında for döngüsüne geri dönderir.
#    print(i)    

#/////////////////////////////////////////////////////////////////////////////////


#liste=[[1,2,3],[4,5,6],[7,8,9,10],[10,11,12,13,14]]
#liste1=[x for i in liste  for x in i]

#print(liste1)

#/////////////////////////////////////////////////////////////////////////////////////


#print("*************KULLANICI GİRİŞİ********************")
#sys_kullanıcıadı="BATUHAN"
#sys_şifre="12345"
#girişhakkı=3

#while True:
 #   kullanıcıadı=input("Kullanıcı Adı:")
  #  parola=input("Parola:")
  #  if(sys_kullanıcıadı==kullanıcıadı and sys_şifre !=parola):
   #     print("Parola Hatalı Tekrar Deneyiniz!\n")
    #    girişhakkı-=1
    #elif(sys_kullanıcıadı!=kullanıcıadı and sys_şifre ==parola)   :
     #   print("Kullanıcı Adı Hatalı Tekrar Deneyiniz!!\n")
      #  girişhakkı-=1
    #elif(sys_kullanıcıadı!=kullanıcıadı and sys_şifre !=parola) :
     #   print("Kullanıcı Adı ve Parola Hatalı \n ")    
      #  girişhakkı-=1
        
    #else:
     #   print("Hoşgeldin {}".format(kullanıcıadı))
      #  break
    #if(girişhakkı==0):
     #   print("Çok fazla hatalı giriş yaptınız!!!")
      #  break

#//////////////////////////////////////////////////////////////////////////////

#print("Faktöriyel Bulma Programı")
#while True:
#    sayi=int(input("Faktöriyelini almak istediğiniz sayıyı giriniz:"))
#    faktöriyel=1
#    for i in range(2,sayi+1):
#        faktöriyel*=i
#        print("faktöriyel:",faktöriyel)

#////////////////////////////////////////////////////////////////////////////////

#a=1
#b=1
#fibonacci=[a,b]
#for i in range(10):
#    a,b=b,a+b
#    fibonacci.append(b)
#print(fibonacci)

#/////////////////////////////////////////////////////////////////////////////////

#sayı = input("Sayı:")
#basamak_sayisi = len(sayı)
#sayı = int(sayı)
#basamak = 0
#toplam = 0

#gecici_sayı = sayı

#while (gecici_sayı > 0):
    
#    basamak = gecici_sayı % 10
    
#    toplam += basamak ** basamak_sayisi
    
#   gecici_sayı //= 10
    

#if (toplam == sayı):
#    print(sayı,"bir armstrong sayısıdır.")
#else:
#    print(sayı,"bir armstrong sayısı değildir.")

#////////////////////////////////////////////////////////////////////////////////   

#  ÇARPIM TABLOSU
#for i in range(1,11):
#    for j in range(1,11):
#        print("{} X {} = {}".format(i,j,i*j))  

#//////////////////////////////////////////////////////////////////////////////////
#toplam = 0

#while True:
    
#    sayı = input("Sayı:")
    
#    if (sayı == "q"):
#        break
#    sayı = int(sayı)
    
#    toplam += sayı
    
#print("Girdiğiniz Sayıların Toplamı:",toplam)

#////////////////////////////////////////////////////////////////////////////////////

#for i in range(1,101):
#    if(i%3 != 0):
#        continue
#    print("i:",i)

#/////////////////////////////////////////////////////////////////////////////////////

#liste={i for i in range(1,101)  if i %2==0}
#print(liste)

#/////////////////////////////////////////////////////////////////////////////////////

#liste=[8,9,3,4,5,11,10]
#liste.sort()# Ögeleri küçükten büyüğe sıralar.Reverse kullanılırsa büyükten küçüğe sıralar.
#liste.insert(5,17)# Konuma öge ekler. İlk sırada indeks belirtir.
#liste.pop(1)#Öğeyi indeks numarasına göre kaldırır.
#liste.append(19)#Listenin sonuna içerdeki öğeyi ekler.
#liste.reverse()#Listeyi ters çevirir.

#////////////////////////////////////////////////////////////////////////////////////////
    
#////////////////////////////////////FONKSİYONLAR//////////////////////////////////////// 
#def selamla(isim):
#    print("İsminiz:",isim)

#selamla("batuhan")

#def toplam(a,b,c):
#    print("Toplamları",a+b+c)
#toplam(5,4,3)    



#FONKSİYONLU FAKTÖRİYEL BULMA
#def faktöriyel():
#    faktöriyel=1
#    sayi=int(input("Faktöriyeli alınacak sayıyı giriniz:"))
#    if(sayi==0 or sayi==1):
#        print("Faktöriyel: ",faktöriyel)
#    else:
#        while(sayi>1):
#            faktöriyel*=sayi
#            sayi-=1
#            if(sayi-1==0):
#              print("Faktöriyel:",faktöriyel)
#faktöriyel()


#/////////////////////////////////DEĞER DÖNDEREN FONKSİYONLAR//////////////////////////////////////
#def toplama(a,b,c):
#    a=int(input("Birinci sayi:"))
#    b=int(input("İkinci sayi:"))
#    c=int(input("üçüncü sayı:"))
#    return a+b+c 


#def bölme(x):
#    bölen=float(input("Bölen sayıyı seçiniz:"))
#    return  x/bölen      # Return den sonra hiçbir fonksiyon çalışmaz.
#print(bölme(toplama(5,4,7)))


#def toplama(*a):
#    toplam=0
#    for i in a:
#        toplam+=i
#        print(toplam)
#toplama(1,2,3)        

#d=5
#def fonksiyon():
#    global d
#    d=3
#    print(d)
#    return d

#fonksiyon()  

#/////////////////////////////LAMBDA////////////////////////////////// 

#çiftsayi= lambda x=int(input("sayi giriniz")): x%2== 0 
         
#print(çiftsayi())

#terscevir= lambda s=input("Liste oluşturun:"):s[::-1]
#print(terscevir())
 

#/////////////////ASAL SAYI KONTROLÜ//////////////////////////////////
#def asal_mı(sayı):
#    if(sayı==1):
#        return False
#    elif(sayı==2):
#           return True
#    else:
#        for i in range(2,sayı):
#           if(sayı % i==0):
#                return False
#        return True
  
#while True:
#     sayi=input("Sayıyı giriniz:")
#     if(sayi=="q"):
#          print("Uygulamadan çıkıldı.")
#          break
#     else:
#          sayi=int(sayi)
#     if(asal_mı(sayi)):
#          print(sayi,"Asal sayıdır.")
#     else:
#          print(sayi,"Asal değildir.")     



#/////////////////////TAM BÖLEN BULMA//////////////////////////////////
#def  tbb(sayı):#tbb-->>TAM BÖLENLERİ BULMA
#    tambolen=[]

#    for i in range(2,sayı+1):
#        if(sayı %i ==0 ):
#            tambolen.append(i)
            
#    return tambolen

#while True:
#    sayı=int(input("Sayı giriniz:"))
#    if(sayı ==0):
#        print("programdan çıkılıyor.")
#        break
#    else:
#        print("tam bolenler",tbb(sayı))    



#//////////////////MÜKEMMEL SAYI////////////////////    
#def mukemmelsayi(sayı):      #1+2+3=6 Bir sayının bölenleri toplamı kendisine eşitse mükemmel sayıdır.
#    toplam=0
#    for i in range(1,sayı):
#        if(sayı%i==0):
#            toplam+=i
#    return toplam==sayı

#for i in range(1,1001):
#    if(mukemmelsayi(i)):
#        print("Mükemmel sayı:",i)

#//////////////EBOB BULMA/////////////////////////
#def ebob(sayı1,sayı2):
#i=1
#ebob=1
#sayı1=int(input("Birinci sayıyı giriniz:"))
#sayı2=int(input("İkinci sayıyı giriniz:"))
#while (i<=sayı1 and i<=sayı2):
#    if(not (sayı1%i) and not (sayı2%i)):
#     ebob=i
#    i+=1
      

#print("Ebob:",ebob(sayı1,sayı2))  



#//////////////////////////EKOK BULMA//////////////////////////////
#def ekok_bulma(sayı1,sayı2):
    
#    i = 2
#    ekok = 1
#    while True:
#        if (sayı1 % i == 0 and sayı2 % i == 0):
#            ekok *= i
#            sayı1 //= i
#            sayı2 //= i#


#        elif (sayı1 % i ==  0 and sayı2 % i != 0):
#            ekok *= i
#            sayı1 //= i


#        elif (sayı1 % i != 0 and sayı2 % i == 0):
#            ekok *= i

#            sayı2 //= i
#        else:
#            i += 1
#        if (sayı1 == 1 and sayı2 == 1):
#            break
#    return ekok

#sayı1 = int(input("Sayı-1:"))
#sayı2 = int(input("Sayı-2:"))

#print("Ekok:",ekok_bulma(sayı1,sayı2))



#//////////////////////SAYI OKUMA/////////////////////////////////
#birler =  ["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
#onlar = ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]

#def okunus(sayı):
#    birinci = sayı % 10
#    ikinci = sayı // 10
    
#    return onlar[ikinci] + " " + birler[birinci]

    
#sayı =  int(input("Sayı:"))

#print(okunus(sayı))

#//////////////////////PİSAGOR BULMA////////////////////////
#def pisagor_bulma():
    
#    pisagor_listesi = list()
#    for i in range(1,101):
#        for j in range(1,101):

#           c = (i ** 2 + j ** 2) ** 0.5
#          if (c == int(c) ):
#            pisagor_listesi.append((i,j,int(c)))
#     return pisagor_listesi

#for i in pisagor_bulma():
#    print(i)    


#////////////////////////////MODÜL KULLANIMI////////////////////////////////

# import Modülün Adı
# dir (Modülün Adı) -->> Modülün içindeki fonksiyonları gösterir.
# help(Modülün Adı) -->> Modüldeki fonskiyonların ne iş yapığını gösterir.
# Modül Adı.Fonksiyon Adı() -->>Modüldeki fonksiyonu çağırır.
# import Modül Adı as Bizim çağırmak istediğimiz isim -->> Modüle istediğimiz ismi verip o isimle çağırmamızı sağlar.
# from Modül Adı import* -->> Modüldeki fonksiyonları modül adı kullanmadan kullanmamızı sağlar.-->>factorial()-->> Modül adı kullanmadan faktöriyel fonksiyonunu çağırdık.
# from Modül Adı import* çağırmak istediğimiz fonksiyon isimleri-->x,y-->> Modülden dilediğimiz fonksiyonu araya virgül koyarak çağırırız fakat sadece çağırdığımız fonksiyonları kullanırız.



#/////////////////////////////////////SAYI TAHMİN OYUNU///////////////////////////////////////
#import random                               #BİNARY SEARCH İLE 1,1000 ARASINDAKİ BİR SAYIYI YAKLAŞIK 10 ADIMDA TAHMİN EDEBİLİRİZ.   
#import time                                 #BINARY SEARCH-->>İKİ SAYININ ORTASI SÖYLEEREK TAHMİN ARALIĞI DARALTILIR.
#print("SAYI TAHMİN OYUNUNA HOŞGELDİNİZ!!")
#tahminhakkı=10
#rastgelesayı=random.randint(1,2000)

#while True:
#    tahmin=int(input("Birle İkibin arasında tahmininizi giriniz:"))

#    if(rastgelesayı>tahmin):
#        print("Bilgiler sorgulanıyor..")
#        time.sleep(1)
#        print("Daha büyük bir sayı söyleyiniz")
#        tahminhakkı-=1
#    elif(rastgelesayı<tahmin):
#        print("Bilgiler sorgulanıyor...")
#        time.sleep(1)
#        print("Daha küçük bir sayı söyleyiniz")
#        tahminhakkı-=1
#    else:
#        print("Bilgiler sorgulanıyor...")
#        time.sleep(1)
#        print("Tebrikler sayınız:",tahmin)
#        break    
#    if(tahminhakkı<0):
#        print("Tahmin hakkınız bitti.")
#        print("Doğru sayı :",tahmin)
#        break    

#import math

#print("Hesap Makinası\n1-)Üs Alma\n2-)Logaritma Alma\n3-)Faktöriyel Alma\n4-)e'nin üssünü alma\n5-)Sinüs Alma\n6-)Cosinüs Alma\n7-)Tanjant Alma\n8-)Permütasyon Alma\n9-)Karekök Alma\n10-)Toplama\n11-)Çarpma")
#("Yapmak istediğiniz işlemi seçiniz:")
#while True:
#  sayı=int(input("Yapmak istediğiniz işlemi seçiniz:"))
#  if(sayı==1):
#    a=int(input("Tabanı giriniz:"))
#    b=int(input("Üssü giriniz:"))
#    print(math.pow(a,b))
    
    
#  elif(sayı==2):
#      a=int(input(" e tabanında logaritması alınacak sayıyı giriniz."))
#      print(math.log(a))
      

#  elif(sayı==3):  
#      a=int(input("Faktöriyeli alınacak sayıyı giriniz."))
#      print(math.factorial(a))
      

#  elif(sayı==4):
#      a=int(input("e nin almak istediğiniz kuvvetini giriniz."))
#      print(math.exp(a))
     

#  elif(sayı==5):
#      pi=3.141592
#      a=int(input("Sinüsü alınacak açıyı giriniz."))
#      a=(pi*a)/180
#      print(math.sin(a))
      

#  elif(sayı==6):
#      pi=3.141592
#      a=int(input("Kosinüsü alınacak açıyı giriniz."))
#      a=(pi*a)/180
#      print(math.cos(a))
      

#  elif(sayı==7):
#      pi=3.141592
#      a=int(input("Tanjantı alınacak açıyı giriniz."))
#      a=(pi*a)/180
#      print(math.tan(a))
      

#  elif(sayı==8):
#      a=int(input("Permütasyonu alınacak sayıyı giriniz."))
#      b=int(input("Sıralama değişkenini giriniz"))
#      print(math.perm(a,b))
      

#  elif(sayı==9):
#      a=int(input("Karekökü alınacak sayıyı giriniz."))

#      print(math.sqrt(a))

#  elif(sayı==10):
#    import modul1 
#    print(modul1.toplama())  

#  elif(sayı==11):
#     import modul1    
#     print(modul1.bolum())
#  else:
#    print("Geçersiz işlem!!")
#    print("Lütfen geçerli bir işlem tuşlayınız:")
   
    
#def double(x):
#    return x*2

#map(double,[1,2,3,4,5])
#list=list(map(double,[1,2,3,4,5]))
#print(list)

#x=list(map(lambda x:x**2,(1,2,3,4,5)))
#print(x)



#/////////////////////////////////////GÖMÜLÜ FONKSİYONLAR////////////////////////////////////////////////////
#MAP(fonksiyon,liste yada demet) içerisine bir fonksiyon bide üzerine gezinebileceğimiz veri girer.Verilerin üzerinde sırasıyla dolanarak fonksiyonu uygular.
#liste1=[1,2,3,4,5,6]
#liste2=[2,4,6,8]
#liste3=[3,6,9,12,15]
#a=list(map(lambda x,y:x*y,liste1,liste2))
#b=list(map(lambda x,y,z:x*y*z,liste1,liste2,liste3))
#print(b)


#REDUCE(fonksiyon,liste yada demet) içerisindeki fonksiyonu soldan başlayarak listenin ilk iki elemanına uygular daha sonra çıkan sonucu üçüncü elemana uygular ve böyle devam eder sonunda bir değer döndürür.
#from functools import reduce
#a=reduce(lambda x,y:x*y,[1,2,3,4,5])
#print(a)


#def maksimum(x,y):
#    if(x>y):
#        return x
#    else:
#        return y
    

#from functools import reduce
#a=reduce(maksimum,[1,5,8,7,5,5,4,8])
#print(a)

#filter(fonksiyon,liste) sadec true olan değerleri döner.
#def asal_mı(x):
#    i=2
#    if(x==1):
#        return False
#    elif(x==2):
#        return True
#    else:
#        while(i<x):
#            if(x%i==0):
#                return False
#            i+=1
#        return True
    
    
#print(list(filter(asal_mı,range(1,100))))

#zip fonksiyonu birden fazla listeyi birleştirir.
#liste1=[1,2,3,4,5,6]
#liste2=[5,6,7,8,9,10]
#liste3=["python","java","C","C++"]
#a=list(zip(liste1,liste2,liste3))
#print(a)

#liste1=[1,2,3,4]
#liste2=["python","java","C","C++"]
#for i,j in zip(liste1,liste2):
#    print("i:",i,"j:",j)



#enumerate(İçerisine sıralı veri verilir ve indeksiyle beraber çıktısını verir.)

#liste=["python","java","C","C++"]
#a=list(enumerate(liste))
#print(a)

#liste=["a","b","c","d","e","f"]
#for index,eleman in enumerate(liste):
#    if(index%2==0):
#        print("Eleman:",eleman)


#all ---->>> all eğer tüm değerler True ise True dönderir ve tek False değerde False dönderir.
#any ---->>> any eğer tüm değerler False ise False dönderir ve tek True değerde True dönderir.

#liste=[False,False,True,False]
#print(any(liste))

#liste=[False,False,True,False]
#print(all(liste))





#////////////////////////////////////////DİKDÖRTGEN ALANI HESABI///////////////////////////////////////////
#liste=[(3,4),(10,3),(5,6),(1,9)]
#a=list(map(lambda x:x[1]*x[0],liste))
#print(a)




#////////////////////////////////////Üçgen Mi/////////////////////////////////////////
#liste=[(3,4,5),(6,8,10),(5,1,3)]
#def ucgen(liste):
#    if(abs(liste[0]+liste[1]>liste[2]) and abs(liste[0]+liste[2]>liste[1]) and abs(liste[1]+liste[2]>liste[0])):
#        return True
#    else:
#        return False
    
#print(list(filter(ucgen,liste) ))




#liste=[1,2,3,4,5,6,7,8,9,10]
#x=list(filter(lambda x:x%2==0,liste))
#from functools import reduce
#print(reduce(lambda x,y:x+y,x))


#isimler=["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
#soyisimler=["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]
#for a,b in zip(isimler,soyisimler):
#    print(a , b)


#///////////////////////////////İLERİ SEVİYE SAYILAR//////////////////////////////////////////
#10'luk taban ----------->>> 2'lik taban ------->>> bin()
#10'luk taban ----------->>> 16'lık taban ------->>> hex()
#abs() -------------->>> Mutlak Değer
#round()-------------->>> En yakın tam sayıya yuvarlar
#max() ----------------->>> En büyük sayıyı dönderir.
#min() ----------------->>> En küçük sayıyı dönderir.
#sum() ------------------>>> Gönderilen liste yada demetleri toplar.
#pow() ------------------->>> Üs alır.

#//////////////////////////////İLERİ SEVİYE STRİNGLER//////////////////////////////////////
#.upper() ------------------>>> Tüm karakterleri büyük yazar.
#.lower() ------------------>>> Tüm karakterleri küçük yazar.

#.replace(a,b) -------------->>> Tüm a karakterlerini b'e çevirir.
#.print("batuhan".replace("han","baba"))    

#.startswith() ----------------->>> İstediğimiz karakterle başlıyorsa True yoksa False değeri dönderir.
#.endwith() ------------------>>> İstediğimiz karakterle bitiyorsa False yoksa True değeri dönderir.
#.split(a) -------------------->>> Verilen a değerine göre stringi parçalar ve listeye atar.
#.strip(x)----------------------->>> Stringin başında ve sonunda bulunan x değerlerini siler.
#.lstrip(x)---------------------->>> Stringin basşındaki x değerlerini siler.
#.rstrip(x) ----------------------->>> Stringin sonundaki x değerlerini siler.

#.join(x)----------------------->>> Listenin her elemanını verdiğimiz değerle birleştirir.
#liste=["T","B","M","M"] 
#print(".".join(liste))

#.count(x) ----------------->>> Stringin içindeki x değerlerini sayar.
#.count(x,indeks) ----------->>> Stringin içindeki x değerini verilen indeksten itiaren sayar.
#.find(a) ------------------->>> Stringin içindeki a değerini baştan itibaren arar ve ilk bulduğu indeksi bize dönderir.Bulamazsa -1 dönderir.
#.rfind(a) -------------------->>> Stringin içindeki a değerini sondan itibaren arar ve ilk bulduğu indeksi bize dönderir.Bulamazsa -1 dönderir.


#//////////////////////////////KÜMELER////////////////////////////////////////
#set()--->>> Kümeye dönüştürür ayrıca bir değişkeni süslü parantezle tanımlarsak küme veri tipi oluşur.
# x={1,2,1,1,2,2,4,5,6,1,5}
# print(type(x))
#Kümelerde her elemandan yalnızca bir tane bulunabilir.
# liste=[1,2,1,1,2,2,4,5,6,1,5]
# x=set(liste)
# print(x)
# x=set("PYTHON PROGRAMLAMA DİLİ")
# print(x)


#x={1,2,3,4,5,6}
#x.add(7)--->>> Kümelere eleman eklemek için kullanılır.


#.difference alttaki örnek için küme1 de olup küme2 de olmayan verileri ekrana bastırır.
# küme1={1,-5,9,17,-21,34,10}
# küme2={1,5,9,17,65,34,10}
# print(küme1.difference(küme2))


#x.difference_update(y)--->>> x kümesinin y den farklı elemanlarını alıp bu elemanlarla yeni bir x kümesi oluşturur.
# x={1,-5,9,17,-21,34,10}
# y={1,5,9,17,65,34,10}
# x.difference_update(y)
# print(x)


#x.discard()--->>>parantezin içine girdiğimiz veriyi kümeden siler.
# x={1,-5,9,17,-21,34,10}
# x.discard(-21)
# print(x)


#x.intersection(y)--->>>x ve y de ortak elemanları bulur.
# x={1,-5,9,17,-21,34,10}
# y={1,5,9,17,65,34,10}
# print(x.intersection(y))


#x.intersection_update(y)--->>>x ve y de ortak elemanları bulup ortak elemanları x e atar.
# x={1,-5,9,17,-21,34,10}
# y={1,5,9,17,65,34,10}
# x.intersection_update(y)
# print(x)



#x.isdisjoint.y--->>>x ve y nin kesişim kümesi varsa false yoksa true dönderir.
# x={1,-5,9,17,-21,34,10}
# y={1,5,9,17,65,34,10}
# z={3,40,50}
# print(x.isdisjoint(y))
# print(x.isdisjoint(z))



#x.issubset(y)--->>>x, y nin alt kümesiyse true değilse false dönderir.
# x={1,2,3,4}
# y={1,2,3,4,5,6}
# print(x.issubset(y))


#x.union(y)--->>> x ve y nin birleşim kümesini dönderir , aynı elemanlar yalnızca bir kere yazılır.
# x={1,-5,9,17,-21,34,10}
# y={1,5,9,17,65,34,10}
# print(x.union(y))


#x.update(y)--->>> x ve y nin birleşim kümesini x'e atar.
# x={1,-5,9,17,-21,34,10}
# y={1,5,9,17,65,34,10}
# x.update(y)
# print(x)

#///////////////////////LİSTE FONKSİONLARI////////////////////////
# x.extend(y)--->>> y nin tüm elemanlarını x e atar.
# x=[1,2,3,4,5]
# y=[2,5,6,7,8,9]
# x.extend(y)
# print(x)


#x.insert(index,eklemek istediğimiz veri)--->>> Listenin istediğimiz indeksine veri ekler.
# x=[1,2,3,4,5]
# x.insert(2,9)
# print(x)


# x.pop()---->>>>Parantezin içi boş bırakılırsa sondaki elemanı yoksa da parantezin içindeki indexteki elemanı atar.
# x=[1,2,3,4,5]
# x.pop(1)
# print(x)



#x.remove(1)--->>>Listeden parantez içindeki değeri atar.
# x=[1,2,3,4,5]
# x.remove(2)
# print(x)



#x.index(b,a)--->>>a değeri girilmezse 0. indeksten itibaren b değerini arar ve bulduğu indeksi yazdırır.a elemanı varsa a'nıncı indeksten başlayarak b değerini ilk bulduğu indeksi dönderir ancak indeks sırası yine sıfırdan başlar yani a dan sonra devam eder,a'yı başlangıç indeksi saymaz.
# x=[1,2,3,2,4,5,6,1,5,2]
# print(x.index(2,6))

#x.count(a)--->>>x listesinde a değerinin kaç defa geçtiğini sayar.

#x.sort()--->>>elemanları küçükten büyüğe sıralar eğer stringse alfabetik olarak sıralar.Reverse=True ifadesi parantez içine konulursa büyükten küçüğe sıralar.
# x=[1,2,3,2,4,5,6,1,5,2]
# x.sort(reverse=True)
# print(x)


