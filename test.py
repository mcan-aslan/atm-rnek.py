

print("ATM \n"
      "İşlemler \n"
      "(0) çıkmak için basın\n"
      "(1) bakiye sorgulama\n"
      "(2) para çekme\n"
      "(3) para yatırma \n")


bakiye = 500

while True:
    islem = input("yapacağınız işlemi seçiniz: ")

    if islem == "0":
        print("çıkılıyor...")
        break

    elif islem =="1":
        print("bakiyeniz:" + str(bakiye))
        break

    elif islem == "2":
        cekme = int(input("çekeceğiniz miktarı giriniz: "))
        bakiye -= cekme
        print("bakiyeniz " + str(bakiye) + " olmuştur")
        # break?
        if cekme>bakiye:
            print("bakiyeniz yetersizdir ")
            break

    elif islem =="3":
        yatir= int(input("yatıralacak miktarı giriniz: "))
        bakiye += yatir
        print("bakiyeniz " + str(bakiye) + " olmuştur")
