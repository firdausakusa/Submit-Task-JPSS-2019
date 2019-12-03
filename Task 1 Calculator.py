print("Ini adalah kalkulator sederhana")

while True:
    a = int(input("Masukkan bilangan pertama: "))
    b = int(input("Masukkan bilangan kedua: "))

    #Menu Operasi
    print("Pilih Operasi")
    print("1.Jumlah")
    print("2.Kurang")
    print("3.Kali")
    print("4.Bagi")

    #Meminta input dari user
    choice = (input ("masukan pilihan (1/2/3/4): "))

    if choice == '1':
        print(a, "+", b, "=", a+b)

    elif choice == '2':
        print(a, "-", b, "=", a-b)

    elif choice == '3':
        print(a, "*", b, "=", a*b)

    elif choice == '4':
        print(a, "/", b, "=", a/b)

    else :
        print("Input Salah")
    
    d = (input("mulai lagi (Y/N): "))
    if d == 'N':
        break

    else:
        True





