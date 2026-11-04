# variabel dan tipe data
nama_mhs = input ("masukkan nama")
kelas = input ("kelas")


nalgoritma =int(input("Masukkan Nlai Algoritma :"))
nagama =int(input("Masukkan Nilai Agama :"))
nbasisdata =int(input("Masukkan Nilai Basis Data :"))
nbahasainggris =int(input("Masukkan Nilai Bhasa Inggris :"))
nbahasaindo =int(input("Masukkan Nilai Bahasa Indonesia :"))
nlogikainformasi =int(input("Masukkan Nilai Logika Informasi :"))
npancasila =int(input("Masukkan nilai Pancasila :"))
rata_rata = (nalgoritma +nagama + nbasisdata + nbahasainggris + nbahasaindo + nlogikainformasi + npancasila) / 7
print(rata_rata)

# penentuan lulus atau tidak
if rata_rata >=80 and rata_rata <=90:
    # kondisi jika terpenuhi
    # maka
    print("Nilai : A")
elif rata_rata >=70 and rata_rata <= 80:
    print("Nilai: B")
elif rat_rata >=50 and rata_rata <= 70:
    print("Nilai: C")
elif rata_rata >=40 and rata_rata <=50:
    print("Nilai: D")


else:
    # cukup menampilkan hasil
    # maka
    print("Nilai : E")