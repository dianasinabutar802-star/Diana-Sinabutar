# Input data mahasiswa
tugas = float(input("Nilai TUGAS : "))
uts = float(input("Nilai UTS : "))
uas = float(input("Nilai UAS : "))
kehadiran = float(input("Kehadiran : "))

# Hitung nilai akhir
nilai_akhir = (0.20 * tugas) + (0.30 * uts) + (0.50 * uas)

# Ekspresi logika untuk syarat
lulus = nilai_akhir >= 75 and kehadiran >= 80
predikat = nilai-akhir >= 85 and kehadiran >= 90 and nilai_akhir % 2 ==0

# Tentukan status
if predikat :
  status = "LULUS DENGAN PREDIKAT"
elif lulus :
  status = "LULUS"
else :
  status = "BELUM LULUS"

# Tampilkan ouput
print(Nilai_akhir : ", nilai-akhir)
print("Status : ", status)
