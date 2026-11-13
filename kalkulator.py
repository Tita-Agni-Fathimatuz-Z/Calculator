print("=== KALKULATOR ===")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
pilihan = input("Masukkan pilihan:")
angka1 = float(input("Masukkan angka pertama:"))
angka2 = float(input("Masukkan angka kedua:"))
if pilihan == "1":
    hasil = angka1 + angka2
    print("Hasil:", hasil)
elif pilihan == "2":
    hasil = angka1 - angka2
    print("Hasil:", hasil)
elif pilihan == "3":
    hasil = angka1 * angka2
    print("Hasil:", hasil)
elif pilihan == "4":
    hasil = angka1 / angka2
    print("Hasil:", hasil)