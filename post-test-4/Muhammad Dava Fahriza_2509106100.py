nama = "Muhammad dava fahriza"
nim = "2509106100"

for i in range(3):
    nama = input("Masukkan nama: ")
    nim = input("Masukkan NIM: ")
    if nama == nama and nim == nim:
        print("anda berhasil login")
        break
    else:
        print("Login gagal!")
else:
    print("batas login telah habis tunggu beberapa saat")

n = int(input("mau beli berapa furnetur?: "))

harga_sofa = 500000
harga_meja_belajar = 250000   
harga_rak_lemari = 150000   
total_harga = 0

for i in range(1, n + 1):
    print(f"\nPilih furnitur yang anda inginkan-{i}:")
    print("1. Rp 500.000 (harga sofa)")
    print("2. Rp 250.000 (harga meja belajar)")
    print("3. Rp 150.000 (harga rak lemari)")
    
    pilihan = int(input("pilih furnitur(1/2/3): "))

    if pilihan == 1:
        total_harga += harga_sofa
    elif pilihan == 2:
        total_harga += harga_meja_belajar
    elif pilihan == 3:
        total_harga += harga_rak_lemari
    else:
        print("Pilihan tidak sesuai. Tiket ini tidak ada.")

print("========================================")
print("============TOTAL HARGA=================")
print("========================================")
print(f"Total harga semua furnitur: Rp {total_harga:,}")
print("========================================")
print("============TERIMAKASIH=================")
print("========================================")