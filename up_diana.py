# Program Pemesanan Tiket Bioskop
# Nama : Diana

print("=== APLIKASI PEMESANAN TIKET BIOSKOP ===")
print("Reguler : Rp35.000")
print("VIP     : Rp50.000")
print("Premium : Rp75.000")
print("Diskon 10% jika beli lebih dari 3 tiket")
print("==========================================")

while True:
    # 1. Input Nama Pelanggan
    nama = input("\nMasukkan nama pelanggan: ")

    # 2. Input Jenis dan Jumlah Tiket
    print("Pilih jenis tiket: Reguler / VIP / Premium")
    jenis = input("Masukkan jenis tiket: ")
    jumlah = int(input("Masukkan jumlah tiket: "))

    # 3. Tentukan Harga (Percabangan)
    if jenis.lower() == "reguler":
        harga = 35000
    elif jenis.lower() == "vip":
        harga = 50000
    elif jenis.lower() == "premium":
        harga = 75000
    else:
        print("Jenis tiket tidak valid!")
        continue

    total = harga * jumlah

    # 4. Cek Diskon (Percabangan)
    if jumlah > 3:
        diskon = total * 0.10
        total_bayar = total - diskon
        print("Mendapatkan diskon 10%!")
    else:
        diskon = 0
        total_bayar = total
        print("Tidak mendapatkan diskon, membayar harga normal.")

    # Menampilkan Hasil
    print("\n--- STRUK PEMBAYARAN ---")
    print("Nama Pelanggan :", nama)
    print("Jenis Tiket     :", jenis)
    print("Jumlah Tiket    :", jumlah)
    print("Total Bayar     : Rp", int(total_bayar))
    print("------------------------")

    # 5. Proses Berulang
    lagi = input("\nAda pelanggan lain? (y/n): ")
    if lagi.lower() != "y":
        print("\nTerima kasih, program selesai!")
        break