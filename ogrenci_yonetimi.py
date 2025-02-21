ogrenciler = []

def ogrenci_ekle(ad, soyad, numara, bolum, not_ort):
    ogrenci = {
        "Ad": ad,
        "Soyad": soyad,
        "Numara": numara,
        "Bolum": bolum,
        "Not Ortalaması": not_ort
    }
    ogrenciler.append(ogrenci)
    print(f"{ad} {soyad} başarıyla eklendi!\n")

def ogrenci_listele():
    if not ogrenciler:
        print("Henüz öğrenci eklenmedi.\n")
        return
    for ogrenci in ogrenciler:
        print(ogrenci)

def ogrenci_bul(numara):
    for ogrenci in ogrenciler:
        if ogrenci["Numara"] == numara:
            return ogrenci
    return None

def ogrenci_guncelle(numara, yeni_ad, yeni_soyad, yeni_bolum, yeni_not_ort):
    ogrenci = ogrenci_bul(numara)
    if ogrenci:
        ogrenci["Ad"] = yeni_ad
        ogrenci["Soyad"] = yeni_soyad
        ogrenci["Bolum"] = yeni_bolum
        ogrenci["Not Ortalaması"] = yeni_not_ort
        print(f"{numara} numaralı öğrencinin bilgileri güncellendi!\n")
    else:
        print("Öğrenci bulunamadı.\n")

def ogrenci_sil(numara):
    global ogrenciler
    ogrenciler = [ogrenci for ogrenci in ogrenciler if ogrenci["Numara"] != numara]
    print(f"{numara} numaralı öğrenci silindi.\n")

def menu():
    while True:
        print("Öğrenci Yönetim Sistemi\n")
        print("1. Öğrenci Ekle")
        print("2. Öğrencileri Listele")
        print("3. Öğrenci Bul")
        print("4. Öğrenci Güncelle")
        print("5. Öğrenci Sil")
        print("6. Çıkış")
        secim = input("Seçiminizi yapın: ")
        
        if secim == "1":
            ad = input("Ad: ")
            soyad = input("Soyad: ")
            numara = input("Numara: ")
            bolum = input("Bölüm: ")
            not_ort = input("Not Ortalaması: ")
            ogrenci_ekle(ad, soyad, numara, bolum, not_ort)
        elif secim == "2":
             ogrenci_listele()
        elif secim == "3":
            numara = input("Öğrenci Numarası: ")
            ogrenci = ogrenci_bul(numara)
            print(ogrenci if ogrenci else "Öğrenci bulunamadı.\n")
        elif secim == "4":
            numara = input("Öğrenci Numarası: ")
            yeni_ad = input("Yeni Ad: ")
            yeni_soyad = input("Yeni Soyad: ")
            yeni_bolum = input("Yeni Bölüm: ")
            yeni_not_ort = input("Yeni Not Ortalaması: ")
            ogrenci_guncelle(numara, yeni_ad, yeni_soyad, yeni_bolum, yeni_not_ort)
        elif secim == "5":
            numara = input("Öğrenci Numarası: ")
            ogrenci_sil(numara)
        elif secim == "6":
             print("Çıkış yapılıyor...")
             break
        else:
             print("Geçersiz seçim. Tekrar deneyin! \n")
menu()


