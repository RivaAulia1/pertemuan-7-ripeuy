def pangkat():
    bil = int(input("Masukkan suatu bilangan bulat: "))
    p = int(input("Masukkan pangkat yang diinginkan: "))

    for i in range(1, p + 1):
        hasil = bil ** i
        print(f"Hasil {bil} pangkat {i} adalah {hasil}")


from fractions import Fraction

def hitung_pecahan():
    print("Contoh: 2/3 + 5/8 - 13/21")

    try:
        a = Fraction(input("Masukkan pecahan pertama: "))
        b = Fraction(input("Masukkan pecahan kedua: "))
        c = Fraction(input("Masukkan pecahan ketiga: "))

        hasil = a + b - c

        print("Hasil =", hasil)
        print("Desimal =", float(hasil))

    except:
        print("Input salah! Gunakan format a/b")


def fibonacci():
    n = int(input("Masukkan jumlah N: "))
    
    a, b = 0, 1
    print("Barisan Fibonacci:")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()


def kali_n():
    n = int(input("Masukkan angka: "))
    batas = int(input("Sampai perkalian ke: "))

    for i in range(1, batas + 1):
        print(f"{n} x {i} = {n * i}")


while True:
    print("\n=== MENU ===")
    print("1. Pangkat Bilangan")
    print("2. Hitung Pecahan")
    print("3. Barisan Fibonacci")
    print("4. Perkalian N")
    print("0. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        pangkat()
    elif pilihan == "2":
        hitung_pecahan()
    elif pilihan == "3":
        fibonacci()
    elif pilihan == "4":
        kali_n()
    elif pilihan == "0":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid!")
