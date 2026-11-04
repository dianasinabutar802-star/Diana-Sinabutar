
print("====================================")
print("       APLIKASI KASIR RESTORAN")
print("====================================")

total = 0
daftar_pesanan = []

while True:
    print("\n========== MENU MAKANAN ==========")
    print("1. Nasi Goreng  - Rp25.000")
    print("2. Mie Ayam     - Rp15.000")
    print("3. Ayam Geprek  - Rp20.000")
    print("4. Sate Ayam    - Rp30.000")
    print("5. Bakso        - Rp18.000")
    print("0. Selesai Memilih")

    pilihan = int(input("\nPilih menu (0-5): "))

    if pilihan == 0:
        break

    elif pilihan == 1:
        nama = "Nasi Goreng"
        harga = 25000

    elif pilihan == 2:
        nama = "Mie Ayam"
        harga = 15000

    elif pilihan == 3:
        nama = "Ayam Geprek"
        harga = 20000

    elif pilihan == 4:
        nama = "Sate Ayam"
        harga = 30000

    elif pilihan == 5:
        nama = "Bakso"
        harga = 18000

    else:
        print("Menu tidak tersedia!")
        continue

    jumlah = int(input("Masukkan jumlah pesanan: "))

    if jumlah <= 0:
        print("Jumlah harus lebih dari 0!")
        continue

    subtotal = harga * jumlah
    total += subtotal

    daftar_pesanan.append((nama, jumlah, subtotal))

    print("Subtotal: Rp", subtotal)

print("\n========== STRUK PEMBAYARAN ==========")

for nama, jumlah, subtotal in daftar_pesanan:
    print(nama, "x", jumlah, "= Rp", subtotal)

print("--------------------------------------")
print("Total Belanja: Rp", total)

if total > 200000:
    diskon = total * 20 / 100
    print("Diskon: 20%")
else:
    diskon = 0
    print("Diskon: 0%")

print("Potongan Harga: Rp", int(diskon))

total_bayar = total - diskon

print("--------------------------------------")
print("TOTAL BAYAR: Rp", int(total_bayar))
print("======================================")
print("Terima kasih telah berbelanja!")
print("======================================")
