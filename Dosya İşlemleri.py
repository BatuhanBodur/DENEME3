#file=open("PY Dosya İşlemler.txt","r") #"w" ile ekleme yapılınca dosya sıfırlanır ve yenisi veriler girilir.
#file.write("12345\n")                   #"a" ile ekleme yapılınca varolan dosyanın üzerine ekleme yapılır.
#file.write("Batuhan Bodur\n")
#file.write("Bilgisayar Mühendisliği 2.sınıf\n")
#file.write("YAZILIMCI\n")
#file.write("PC engıneering\n")
#file.write("Mehmet Bodur\n")
#file.write("Utku Bodur")
#file.close()


#for i in file:      #for döngüsü yardımıyla dosya içeriği okunabilir.
#    print(i,end="")
#file.close()

#içerik=file.read() #dosya okumanın bir diğer yolu da read fonksiyonudur.Eğer parantez içine i gibi bir değer atanırsa i bitlik veri okur.
#print(içerik)      #imleci dosyanın sonuna taşıdığı için artarda kullanılırsa ikinci fonksiyon boş dönecektir.
#file.close()


#print(file.readline()) #Yalnızca bir satır yazdırır.Eğer artarda kullanılırsa tüm satırlar tek tek yazdırılabilir.
#file.close()

#print(file.readlines()) #Dosyada ki verileri bir listeye atar.Çıktı köşeli parantez ile verilir.
#file.close()

#file.tell()#Dosyanın kaçıncı bitinde olduğumuzu gösterir.
#file.seek(i)#Dosyanın i'nci indeksine gider.
#with open("PY Dosya İşlemler.txt","r") as file #Bu blok dosyaları otomatik olarak kapatır 

#with open("PY Dosya İşlemler.txt","a") as file # Buradaki a sayesinde imleci direkt dosyaanın sonuna götürürüz.

#with open("PY Dosya İşlemler.txt","r") as file:
    #file.write("Batuhan Bodur\nBilgisayar Mühendisliği\n2.sınıf")
    #file.read(6)
    #file.seek(2)
    #print(file.tell())
    #print(file.read(5))

#with open("PY Dosya İşlemler.txt","r+") as file: #r+ sayesinde hem dosyayı okuyabiir hem dosyaya yazabiliriz.

#with open("PY Dosya İşlemler.txt","r+") as file :
#    print(file.read())


#with open("PY Dosya İşlemler.txt","r+") as file: #Bu blok sayesinde dosyanın başına veri ekleyebiliriz.
   #file.seek(0)
   #file.write("Eklemek istenilen veri")


#with open("PY Dosya İşlemler.txt","r+") as file:#Bu blokta dosyayı satır satır okutup bir listeye atarız.
  #liste=file.readlines()                       #Daha sonra listelerde kullandığımız insert metoduyla istediğimiz indekse yazdırırız.
  #liste.insert(1,"ML\n")
#print(file.read())  

  #file.seek(0)            #Yada writelines ile listeyi dosyamıza direkt olarak yazdırız ve for döngüsüne gerek kalmaz.
  #file.writelines(liste)
  #print(file.read())
   

#///////////////////////////////////HARF NOTU HESAPLAMA///////////////////////////////////////
#def not_hesapla(satır):
#    liste = satır.split(",")
#    isim = str(liste[0])
#    not1 = int(liste[1])
#    not2 = int(liste[2])
#    not3 = int(liste[3])
#    son_not = not1 * (3/10) + not2 * (3/10) + not3 * (4/10)
#    harf = son_not
#    if son_not >= 90:
#        return isim, "AA"
#    elif son_not >= 85:
#        return isim, "BA"
#    elif son_not >= 80:
#        return isim, "BB"
#    elif son_not >= 75:
#        return isim, "CB"
#    elif son_not >= 70:
#        return isim, "CC"
#    elif son_not >= 65:
#        return isim, "DD"
#    elif son_not >= 60:
#        return isim, "FD"
#     else:
#        return isim, "FF"

#with open("PY Dosya İşlemler.txt", "r") as file:
#    eklenecekler_listesi = []
#    for i in file:
#        eklenecekler_listesi.append(not_hesapla(i))

#with open("notlar.txt", "w") as file2:
#    for i in eklenecekler_listesi:
#        file2.write(f"{i[0]} {i[1]}\n")


#with open("Geçenler.txt","w") as file3:
#    for i in eklenecekler_listesi:
#        if(i[1]!="FF"):
#            file3.write(f"{i[0]},{i[1]}\n")
        
#with open("Kalanlar.txt","w") as file4:
#    for i in eklenecekler_listesi:
#        if(i[1]=="FF"):
#          file4.write(f"{i[0]} {i[1]}\n")

          
