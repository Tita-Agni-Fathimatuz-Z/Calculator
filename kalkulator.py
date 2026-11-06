def kalkulator():
    while True:
        print("\n=== KALKULATOR ===")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Pembagian")
        print("4. Perkalian")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "5":
            print("Terima kasih!")
            break

        if pilihan in ["1", "2", "3", "4"]:
            angka1 = float(input("Masukkan angka pertama: "))
            angka2 = float(input("Masukkan angka kedua: "))

            if pilihan == "1":
                hasil = angka1 + angka2
                print("Hasil:", hasil)

            elif pilihan == "2":
                hasil = angka1 - angka2
                print("Hasil:", hasil)

            elif pilihan == "3":
                if angka2 == 0:
                    print("Tidak bisa dibagi dengan nol!")
                else:
                    hasil = angka1 / angka2
                    print("Hasil:", hasil)

            elif pilihan == "4":
                hasil = angka1 * angka2
                print("Hasil:", hasil)

        else:
            print("Pilihan tidak valid!")


kalkulator()