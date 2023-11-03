import os

def txt_fayli_sil():
    fayl_adı = "New Text Document.txt"
    try:
        os.remove(fayl_adı)
        print(f"{fayl_adı} faylı uğurla silindi.")
    except FileNotFoundError:
        print(f"{fayl_adı} faylı tapılmadı.")

def melumat_elave_et(melumat):
    fayl_adı = "New Text Document.txt"
    try:
        with open(fayl_adı, "a") as fayl:
            fayl.write(melumat + "\n")
        print("Məlumat uğurla əlavə olundu.")
    except Exception as e:
        print(f"Məlumat əlavə edilərkən xəta baş verdi: {str(e)}")

def melumat_sayi_goster():
    fayl_adı = "New Text Document.txt"
    try:
        with open(fayl_adı, "r") as fayl:
            melumatlar = fayl.read().splitlines()
            melumat_sayi = len(melumatlar)
            print(f"Basadakı məlumatların sayı: {melumat_sayi}")
    except FileNotFoundError:
        print(f"{fayl_adı} faylı tapılmadı.")

def main():
    while True:
        print("1 - TXT Faylı Sil")
        print("2 - Məlumat Əlavə Et")
        emeliyyat = input("Emeliyyatı seçin (1/2): ")
        
        if emeliyyat == "1":
            txt_fayli_sil()
        elif emeliyyat == "2":
            melumat = input("Əlavə etmək istədiyiniz məlumatı daxil edin: ")
            melumat_elave_et(melumat)
        else:
            print("Yanlış emeliyyat seçdiniz. 1 və ya 2 seçin.")
        
        melumat_sayi_goster()

if __name__ == "__main":
    main()
