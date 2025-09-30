print("================")
print(" PEMBAYARAN UKT ")
print("================")
daftar_nama = "Muhammad Dava Fahrza"
daftar_nim = "2509106100"


Nama = input("Nama: ")
Nim = int(input("Nim: "))
print("anda berhasil login")

UKT = 6000000

print("paket A")
print("paket B")
print("paket C")
print("paket D")
pilih = str(input("pilih paket pembayaran (A/B/C/D): "))

if pilih == "A":
    biaya_admin = 0.01
    jumlah_cicilan = 1

elif pilih == "B":
    biaya_admin = 0.5
    jumlah_cicilan = 2

elif pilih == "C":
    biaya_admin = 0.8
    jumlah_cicilan = 4

elif pilih == "D":
    biaya_admin = 0.12
    jumlah_cicilan = 6

else :
    print("pilihan tidak ada")

Total_bayar = UKT + (UKT * biaya_admin)
Cicilan = Total_bayar / jumlah_cicilan

print("==========================")
print("=== Rincian Pembayaran ===")
print("==========================")
print(f"UKT Pokok        : Rp {UKT:,.0f}")
print(f"Biaya Admin      : {biaya_admin*100:.0f}%")
print(f"Total Bayar      : Rp {Total_bayar:,.0f}")
print(f"Jumlah Cicilan   : Rp {Cicilan:,.0f}")
print(f"Bayar per Cicilan: {jumlah_cicilan:,.0f}")