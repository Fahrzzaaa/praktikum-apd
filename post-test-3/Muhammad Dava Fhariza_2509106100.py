# print("================")
# print(" PEMBAYARAN UKT ")
# print("================")
# daftar_nama = "Muhammad Dava Fahrza"
# daftar_nim = "2509106100"


# Nama = input("Nama: ")
# Nim = int(input("Nim: "))
# print("anda berhasil login")

# UKT = 6000000

# print("paket A")
# print("paket B")
# print("paket C")
# print("paket D")
# pilih = str(input("pilih paket pembayaran (A/B/C/D): "))

# if pilih == "A":
#     biaya_admin = 0.01
#     jumlah_cicilan = 1

# elif pilih == "B":
#     biaya_admin = 0.5
#     jumlah_cicilan = 2

# elif pilih == "C":
#     biaya_admin = 0.8
#     jumlah_cicilan = 4

# elif pilih == "D":
#     biaya_admin = 0.12
#     jumlah_cicilan = 6

# else :
#     print("pilihan tidak ada")

# Total_bayar = UKT + (UKT * biaya_admin)
# Cicilan = Total_bayar / jumlah_cicilan

# print("==========================")
# print("=== Rincian Pembayaran ===")
# print("==========================")
# print(f"UKT Pokok        : Rp {UKT:,.0f}")
# print(f"Biaya Admin      : {biaya_admin*100:.0f}%")
# print(f"Total Bayar      : Rp {Total_bayar:,.0f}")
# print(f"Jumlah Cicilan   : Rp {Cicilan:,.0f}")
# print(f"Bayar per Cicilan: {jumlah_cicilan:,.0f}")



# pilih paket pesawat dengan for loop dan if-else

# jumlah tiket
n = int(input("Masukkan jumlah Tiket: "))

# Harga tiket
harga_A = 1000000  # Tiket Pesawat Jakarta
harga_B = 800000   # Tiket Pesawat Bali
harga_C = 600000   # Tiket Pesawat Malang

# total harga dan jumlah tiap paket
total_harga = 0
count_A = 0
count_B = 0
count_C = 0

# pilihan paket
for i in range(1, n + 1):
    print(f"\nPilih paket harga untuk tiket ke-{i}:")
    print("1. Rp 1.000.000 (Tiket Pesawat Jakarta)")
    print("2. Rp 800.000  (Tiket Pesawat Bali)")
    print("3. Rp 600.000  (Tiket Pesawat Malang)")
    
    pilihan = int(input("Masukkan pilihan (1/2/3): "))
    
    if pilihan == 1:
        total_harga += harga_A
        count_A += 1
    elif pilihan == 2:
        total_harga += harga_B
        count_B += 1
    elif pilihan == 3:
        total_harga += harga_C
        count_C += 1
    else:
        print("Pilihan tidak sesuai. Tiket ini tidak ada.")

# Hitung rata-rata
if n > 0:
    rata_rata = total_harga / n                                                                                         
else:
    rata_rata = 0

# Output hasil
print("\n--- Hasil Penilaian ---")
print(f"Total harga semua tiket: Rp {total_harga:,}")
print(f"Rata-rata harga tiket: Rp {rata_rata:,.2f}")
print(f"Jumlah Tiket Pesawat Jakarta (Rp 1.000.000): {count_A}")
print(f"Jumlah Tiket Pesawat Bali (Rp 800.000): {count_B}")
print(f"Jumlah Tiket Pesawat Malang (Rp 600.000): {count_C}")

