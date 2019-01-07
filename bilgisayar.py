import time
i=0

class bilgisayar():

    def __init__(self, bilgisayar_durum="kapalı"):

        self.bilgisayar_durum = bilgisayar_durum

    def bilgisayarın_sonhali(self):

        print("bilgisayarın son hali = {}".format(self.bilgisayar_durum))

    def bilgisayarı_aç(self):

        if (self.bilgisayar_durum == "kapalı"):
            print("bilgisayar açılıyor..")

            for i in range(0,3):
                time.sleep(0.5)
                print(" . ")
            print("bilgisayar açıldı.")
            self.bilgisayar_durum = "açık"
        else:
            print("bilgisayar zaten açık")

    def bilgisayar_kapat(self):
        if (self.bilgisayar_durum == "açık"):
            print("bilgisayar kapanıyor...")
            self.bilgisayar_durum = "kapalı"
        else:
            print("bilgisayar zaten kapalı")

    def bilgisayar_formatla(self):

        if (self.bilgisayar_durum == "kapalı"):
            print("önce bilgisayarı açın")

        else:
            print("bilgisayar formatlanıyor.. Bu işlem 1 saniye sürebilir....")
            time.sleep(1)
            self.bilgisayar_durum = "kapalı"

    def hesapmakinesi_aç(self):

        if (self.bilgisayar_durum == "kapalı"):
            print("önce bilgisayarı açın")

        else:
            while True:
                print("hesap makinesi açılıyor..")

                print("""

                ***************************

                HESAP MAKİNESİ İŞLEMLERİ 

                1. İŞLEM TOPLAMA

                2. İŞLEM ÇIKARMA 

                3. İŞLEM ÇARPMA

                4. İŞLEM BÖLME

                5. ÇIKMAK İÇİN BASIN

                """)

                a = int(input("ilk sayıyı giriniz : "))

                b = int(input("ikinci sayıyı giriniz : "))

                işlem = input("işlemi giriniz : ")

                if (işlem == "1"):
                    print("{} ile {} toplamı : {} .".format(a, b, a + b))

                elif (işlem == "2"):
                    print("{} ile {} farkı : {} ".format(a, b, a - b))

                elif (işlem == "3"):
                    print("{} ile {} çarpımı : {} ".format(a, b, a * b))

                elif (işlem == "4"):
                    print("{} ile {} bölümü : {} ".format(a, b, a / b))

                elif (işlem == 5):
                    print("hesap makinesinden çıkılıyor..")
                    break
                else:
                    print("GEÇERSİZ İŞLEM SEÇTİNİZ")

    def taşkağıtmakas(self):
        if (self.bilgisayar_durum == "açık"):
            import random

            taşkağıtmakas = ["taş", "kağıt", "makas"]

            taş = taşkağıtmakas[0]
            kağıt = taşkağıtmakas[1]
            makas = taşkağıtmakas[2]
            i = 0
            computer = 0
            player = 0
            btaş = 0
            bkağıt = 0
            bmakas = 0
            oyuncuismi = input("Lütfen oyuncu adınızı giriniz = ")

            def sonuçları_göster():
                if (computer > player):
                    print("{} - {} computer kazanıyor.".format(computer, player))
                    print("""BİLGİSAYAR {} = TAŞ
                           {} = KAĞIT
                           {} = MAKAS

                                SEÇTİ.""".format(btaş, bkağıt, bmakas))
                elif (player > computer):
                    print("{} {} {} kazanıyor.".format(player, computer, oyuncuismi))
                    print("""BİLGİSAYAR {} = TAŞ
                           {} = KAĞIT
                           {} = MAKAS

                                SEÇTİ.""".format(btaş, bkağıt, bmakas))
                else:
                    print("Computer ve {} {} {} berabere".format(oyuncuismi, computer, player))
                    print("""BİLGİSAYAR {} = TAŞ
                           {} = KAĞIT
                           {} = MAKAS

                                SEÇTİ.""".format(btaş, bkağıt, bmakas))

            while True:
                devammı = input("oyuna DEVAM etmek için 1 e ÇIKMAK için q ya SONUÇLAR için 2 ye basın.")

                if (devammı == "1"):

                    gir = input(" taş mı kağıt mı makas mı ")

                    a = random.choice(taşkağıtmakas)

                    print("bilgisayar {} seçti..".format(a))

                    if (gir == taş):

                        if (gir == a):
                            print("berabere. puan alamadınız")
                            btaş += 1
                        elif (a == kağıt):
                            print("kaybettiniz. kağıt taşı sarar.")
                            bkağıt += 1
                            computer += 1
                        elif (a == makas):
                            print("kazandınız. taş makası kırar.")
                            bmakas += 1
                            player += 1

                    elif (gir == kağıt):

                        if (a == gir):
                            print("berabere. puan alamadınız.")
                            bkağıt += 1
                        elif (a == taş):
                            print("kazandınız. kağıt taşı sarar.")
                            player += 1
                            btaş += 1
                        elif (a == makas):
                            print("kaybettiniz. makas kağıdı keser.")
                            bmakas += 1
                            computer += 1

                    elif (gir == makas):

                        if (a == gir):
                            print("berabere. puan alamadınız.")
                            bmakas += 1
                        elif (a == taş):
                            print("kaybettiniz. taş makası kırar.")
                            btaş += 1
                            computer += 1
                        elif (a == kağıt):
                            print("kazandınız. makas kağıdı keser.")
                            bkağıt += 1
                            player += 1
                    else:
                        print("geçersiz işlem")

                elif (devammı == "2"):
                    sonuçları_göster()

                elif (devammı == "q"):
                    print("tekrar bekleriz. sonuçlar birazdan açıklanıyor..")
                    break
                else:
                    print("geçersiz işlem")
                    break

            print("""

                ****************
                SONUÇLAR

                ****************

                BİLGİSAYAR = {}
                {} = {}

                BİLGİSAYAR {} = TAŞ
                           {} = KAĞIT
                           {} = MAKAS

                                SEÇTİ.

            """.format(computer, oyuncuismi, player, btaş, bkağıt, bmakas))

        else:
            print("önce bilgisayarı açın..")

    def vizenotu_hesapla(self):
        if (self.bilgisayar_durum == "açık"):

            while True:
                print("işlem seçiniz = NOTUNUZU HESAPLAMAK İSTİYORSANIZ 1 \n ÇIKMAK İÇİN 2 BASIN.")

                if (işlem == 1):
                    vize1 = float(input("kısa sınav notunuzu girin   : "))
                    vize2 = float(input("vize notunuzu giriniz : "))
                    final = float(input("final notunuzu giriniz : "))

                    vize1 = (vize1 * 30) / 100
                    vize2 = (vize2 * 30) / 100
                    final = (final * 40) / 100

                    sonuç = vize1 + vize2 + final

                    print("SINAV SONUCUNUZ : ", sonuç)

                    if (sonuç >= 90):
                        print("AA ALDINIZ.")
                    elif (sonuç >= 85):
                        print("BA ALDINIZ.")
                    elif (sonuç >= 80):
                        print("BB ALDINIZ.")
                    elif (sonuç >= 75):
                        print("CB ALDINIZ.")
                    elif (sonuç >= 70):
                        print("CC ALDINIZ.")
                    elif (sonuç >= 65):
                        print("DC ALDINIZ.")
                    elif (sonuç >= 60):
                        print("DD ALDINIZ.")
                    elif (sonuç >= 55):
                        print("FD ALDINIZ.")
                    elif (sonuç <= 50):
                        print("FF ALDINIZ , KALDINIZ.")
                    else:
                        print("HATALI GİRİŞ YAPTINIZ.")
                else:
                    print("çıkış yapılıyor...")
                    break
        else:
            print("önce bilgisayarı açın")


print("""
BİLGİSAYARA HOŞGELDİNİZ...

1 = BİLGİSAYARI AÇ
2 = BİLGİSAYARI KAPAT 
3 = BİLGİSAYARIN SON HALİNE BAK
4 = BİLGİSAYARI RESETLE
5 = HESAP MAKİNESİ AÇ
6 = VİZE FİNAL NOTU HESAPLA
7 = TAŞ KAĞIT MAKAS OYNA
q = PROGRAMDAN ÇIK
""")
bilgisayar1 = bilgisayar()
while True:
    işlem = int(input("işlemi giriniz.."))

    if (işlem == "q" or işlem == "Q"):
        print("BİLGİSAYARDAN ÇIKILIYOR....")
        break
    elif (işlem == 1):

        bilgisayar1.bilgisayarı_aç()

    elif (işlem == 2):

        bilgisayar1.bilgisayar_kapat()

    elif (işlem == 3):

        bilgisayar1.bilgisayarın_sonhali()

    elif (işlem == 4):

        bilgisayar1.bilgisayar_formatla()

    elif (işlem == 5):

        bilgisayar1.hesapmakinesi_aç()

    elif (işlem == 6):

        bilgisayar1.vizenotu_hesapla()
    elif (işlem == 7):

        bilgisayar1.taşkağıtmakas()
    else:
        print("geçersiz işlem")

