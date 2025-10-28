total_pendapatan_global = 0
jumlah_costumer_global = 0
last_costumer_global = ""


def hitung_total_harga(nama, harga_paket, jumlah):
    
    total_harga = harga_paket * jumlah
    keterangan = f"Costumer {nama} membeli {jumlah} paket"
    status = "Transaksi berhasil!"
    print("\n=== HASIL PERHITUNGAN ===")
    print(keterangan)
    print(f"Harga per paket: Rp{harga_paket}")
    print(f"Total harga: Rp{total_harga}")
    print(status)
    return total_harga  


def tampilkan_statistik():
    
    data_tersedia = len(data_costumer)
    pendapatan_total = sum(info["total_harga"] for info in data_costumer.values())

    print("\n=== STATISTIK PENJUALAN ===")
    print(f"Jumlah data costumer : {data_tersedia}")
    print(f"Total pendapatan     : Rp{pendapatan_total}")
    print(f"Costumer terakhir    : {last_costumer_global if last_costumer_global else 'Belum ada'}")
    print("=================================\n")


def update_global(nama, total):
    global total_pendapatan_global, jumlah_costumer_global, last_costumer_global
    
    tambahan_pendapatan = total
    tambahan_costumer = 1
    total_pendapatan_global += tambahan_pendapatan
    jumlah_costumer_global += tambahan_costumer
    last_costumer_global = nama


data_costumer = {
    "Dava": {"paket": "Paket 3 Orang", "jumlah": 1, "total_harga": 50000},
    "Fahriza": {"paket": "Paket 6 Orang", "jumlah": 1, "total_harga": 90000}
}

paket = {
    1: ("Paket (A) 1 Orang", 20000),
    2: ("Paket (B) 3 Orang", 50000),
    3: ("Paket (C) 6 Orang", 90000),
    4: ("Paket (D) 8 Orang", 120000)
}

username_asli = "Dava"
password_asli = "100"

print("====== LOGIN SISTEM TIKET KOLAM RENANG ======")
for percobaan in range(3):
    username = input("Masukkan nama: ")
    password = input("Masukkan password: ")
    if username == username_asli and password == password_asli:
        print("Login berhasil!.")
        break
    else:
        print("nama atau password salah")
else:
    print("Anda telah gagal login 3 kali. Program berhenti.")
    exit()

while True:
    print("""
======== MENU UTAMA ========
1. Tambah Data Costumer
2. Lihat Data Costumer
3. Ubah Data Costumer
4. Hapus Data Costumer
5. Keluar
============================
""")
    pilih = input("Pilih menu (1-5): ")

    if pilih == "1":
        print("===== Tambah Data Costumer ====")
        print("Pilih paket tiket:")
        for i, n in paket.items():
            print(f"{i}. {n[0]} - Rp{n[1]}")

        pilih_paket = int(input("Masukkan nomor paket: "))

        if pilih_paket in paket:
            nama = input("Atas nama siapa kak: ")

            if nama in data_costumer:
                print("Nama tersebut sudah terdaftar, silakan gunakan nama lain.")
                continue

            jumlah = int(input("Mau beli berapa paket?: "))
            harga_paket = paket[pilih_paket][1]
            total_harga = harga_paket * jumlah

            data_costumer[nama] = {
                "paket": paket[pilih_paket][0],
                "jumlah": jumlah,
                "total_harga": total_harga
            }

            print("===============TOTAL HARGA================")
            print(f"Paket         : {paket[pilih_paket][0]} x{jumlah}")
            print(f"Harga paket   : Rp{harga_paket}")
            print(f"Total bayar   : Rp{total_harga}")
            print("==========================================")
            print("Data costumer berhasil ditambahkan!")

            
            total_baru = hitung_total_harga(nama, harga_paket, jumlah)
            update_global(nama, total_baru)
            tampilkan_statistik()

        else:
            print("Paket tidak tersedia.")

    elif pilih == "2":
        print("\n=== Data Costumer Kolam Renang ===")
        if not data_costumer:
            print("Belum ada data costumer.")
        else:
            total_semua = 0
            for nama, info in data_costumer.items():
                print(f"Nama: {nama} | Paket: {info['paket']} | Jumlah: {info['jumlah']} | Total Harga: Rp{info['total_harga']}")
                total_semua += info["total_harga"]
            print(f"\nTotal pendapatan: Rp{total_semua}")

    elif pilih == "3":
        print("\n=== Ubah Data Costumer ===")
        if not data_costumer:
            print("Belum ada data costumer.")
        else:
            nama = input("Masukkan nama costumer yang ingin diubah: ")

            if nama in data_costumer:
                print("Pilih paket baru:")
                for i, n in paket.items():
                    print(f"{i}. {n[0]} - Rp{n[1]}")
                pilih_paket = int(input("Masukkan nomor paket: "))

                if pilih_paket in paket:
                    jumlah = int(input("Masukkan jumlah paket baru: "))
                    harga_paket = paket[pilih_paket][1]
                    total_harga = harga_paket * jumlah
                    data_costumer[nama] = {
                        "paket": paket[pilih_paket][0],
                        "jumlah": jumlah,
                        "total_harga": total_harga
                    }
                    print(f"\nData {nama} berhasil diubah!")
                    print(f"Paket baru: {paket[pilih_paket][0]} x{jumlah}")
                    print(f"Total baru: Rp{total_harga}")

                    
                    update_global(nama, total_harga)
                    tampilkan_statistik()
                else:
                    print("Paket tidak tersedia.")
            else:
                print("Nama costumer tidak ditemukan.")

    elif pilih == "4":
        print("\n=== Hapus Data Costumer ===")
        if not data_costumer:
            print("Belum ada data costumer.")
        else:
            nama = input("Masukkan nama costumer yang ingin dihapus: ")
            if nama in data_costumer:
                data_costumer.pop(nama)
                print("Data costumer berhasil dihapus!")
                tampilkan_statistik()
            else:
                print("Nama costumer tidak ditemukan.")

    elif pilih == "5":
        print("Terima kasih, program selesai!")
        tampilkan_statistik()
        break

    else:
        print("Pilihan tidak valid.")
