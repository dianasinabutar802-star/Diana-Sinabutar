# 1. Input nama mahasiswa dan tentukan target
nama = input("Nama : ")

if nama.lower() == "andi":
    target = 70
elif nama.lower() == "budi":
    target = 75
elif nama.lower() == "citra":
    target = 80
else:
    print("Nama tidak ditemukan!")
    exit()

print(f"Target nilai {nama} : {target}")
print("--------------------------")

# 2 & 3. Input nilai, cek target, ulangi maksimal 3x pakai while
percobaan = 1
lulus = False

while percobaan <= 3:
    nilai = int(input(f"Nilai {percobaan} : "))

    if nilai >= target:
        lulus = True
        break
    else:
        print(f"Belum mencapai target, harus remedial!")
        percobaan += 1

# 4. Tampilkan hasil akhir
print("--------------------------")
if lulus:
    print(f"{nama} berhasil lulus setelah {percobaan} kali percobaan!")
else:
    print(f"{nama} tidak lulus setelah 3 kali percobaan!")