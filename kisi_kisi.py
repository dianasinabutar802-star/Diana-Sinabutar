
while True:
    print("\n===== PROGRAM KASIR MINIMARKET =====")

    # Input data barang
    nama_barang = input("Masukkan nama barang: ")
    harga_barang = int(input("Masukkan harga barang: Rp"))
    jumlah_barang = int(input("Masukkan jumlah barang: "))

    # Menghitung total belanja
    total_belanja = harga_barang * jumlah_barang

    # Menentukan diskon
    if total_belanja > 200000:
        diskon = total_belanja * 0.10
    else:
        diskon = 0

    # Menghitung total pembayaran
    total_bayar = total_belanja - diskon

    # Menampilkan hasil transaksi
    print("\n===== STRUK PEMBAYARAN =====")
    print("Nama Barang   :", nama_barang)
    print("Harga Barang  : Rp", harga_barang)
    print("Jumlah Barang :", jumlah_barang)
    print("Total Belanja : Rp", total_belanja)
    print("Diskon        : Rp", int(diskon))
    print("Total Bayar   : Rp", int(total_bayar))

    # Mengulang transaksi
    ulang = input("\nTransaksi pelanggan berikutnya? (ya/tidak): ")

    if ulang.lower() == "tidak":
        print("Terima kasih telah berbelanja!")
        break
