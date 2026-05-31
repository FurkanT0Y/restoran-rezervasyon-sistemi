menu = {}
def menu_olustur():
    Yetkili_AD = input("Yöneticinin ismi: ").upper()
    print(f" Hoşgeldin {Yetkili_AD} Patron  \n")
    while(True):
        yemek = input("Menüye eklemek istediğiniz yemeği giriniz:(Başka yemek yoksa bitti yazınız.) \n").capitalize()
        if (yemek.lower() == "bitti"):
            break
        try:
            fiyat = float(input(f"{yemek} için fiyat giriniz:\n"))
            menu[yemek] = fiyat
        except ValueError:
            print("Hatalı girdiniz. ")
            print("Lütfen sadece sayı giriniz.")
    return menu

yeni_menu = menu_olustur()

print("Yemek Listesi\n")
for yemek, fiyat in yeni_menu.items():
    print(f"{yemek}: {fiyat}TL")

import datetime

toplam_kazanc = 0
musteri_list = []
dolu_masalar = [] 

while(True):
    print("---MÜŞTERİ SİSTEMİ---\n")
    
    while(True):
        masa_no = input("Masa numarası: \n")
        if masa_no in dolu_masalar:
            print(f"!!! Masa {masa_no} şu an dolu. Lütfen başka bir masa seçiniz.\n")
        else:
            break
            
    while(True):
        isim = input("Müşteri İsmi:\n").capitalize()
        musteri_siparisleri = []
        
        while(True):
            siparis = input(f"Masa {masa_no} ({isim}) için sipariş giriniz. Bitirmek için bitir yazın\n").capitalize()
            
            if siparis.lower() == "bitir":
                break

            if siparis in yeni_menu:
                musteri_siparisleri.append(siparis)
                toplam_kazanc += yeni_menu[siparis]
                print(f"=>{siparis} başarıyla eklendi\n")

            else:
                print(f"=>{siparis} menüde yok")
        
        if musteri_siparisleri:
            musteri_list.append(isim)
            with open("siparisler.txt", "a", encoding="utf-8") as siparis_list:
                siparisler_metni = ", ".join(musteri_siparisleri)
                siparis_list.write(f"Müşteri:{isim},Masa No:{masa_no},Siparişler:{siparisler_metni}\n")
        
        ayni_masa = input(f"Masa {masa_no}'de hesaba eklenecek başka müşteri var mı? (var/yok) yazınız.\n")
        if ayni_masa.lower() == "yok":
            dolu_masalar.append(masa_no) 
            break
            
    durum1 = input("Dışarıdan gelecek başka yeni müşteri var mı? (var/yok).\n")
    if(durum1.lower() == "yok"):
        print("Dökümanları inceleyebilirsiniz)")
        break

tarih = datetime.datetime.now().strftime("%d-%m-%y")
with open("gun_sonu.txt", "w", encoding="utf-8") as dosya:
    dosya.write(f"TARİH:{tarih}\n\n")
    dosya.write("--- MASA VE GELİR DETAYLARI ---\n")
    dosya.write("\n".join(musteri_list) + "\n\n")
    dosya.write(f"TOPLAM GENEL GELİR:{toplam_kazanc} TL\n")