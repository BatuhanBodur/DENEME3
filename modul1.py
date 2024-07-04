def bölme():
    bölüm = 0
    sayac = 0
    while True:
        sayı = input("Bölümünü almak istediğiniz sayıyı giriniz (Sonuç için '00' giriniz): ")
        if sayı == '00':
            if sayac == 0:
                print("Hiç veri girmediniz.")
            else:
                print("Toplam bölüm:", bölüm)
                break
        else:
            sayı = float(sayı)
            bölüm+= 1 / sayı
            sayac += 1
    return bölüm









def çarpma():
    çarpım=1
    while True:
        sayı=input("Çarpmak istediğiniz sayıları giriniz(Sonuç için q a basınız.):")
        if(sayı=="q"):    #SIFIR çarpma işlemine dahil edilsin diye sayıyı input alıp else kısmında veri tipi dönüşümü yaptık.
            print("Çarpım:",çarpım)
            break   
        else:
            sayı=int(sayı)
            çarpım=çarpım*sayı
    return çarpım   
 

            
        

def toplama():
    toplam= 0
    while True: 
        sayı = int(input("Toplamak istediğiniz sayıları giriniz(0'a basıldığında işlem gerçekleştirilecektir): "))
        if (sayı == 0):
            print("toplam:",toplam)
            break
        toplam+= sayı
    return toplam

