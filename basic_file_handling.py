
import os

# Menentukan lokasi file TXT di folder yang sama
folder = os.path.dirname(os.path.abspath(__file__))
nama_file = os.path.join(folder, "daftar_buku.txt")

print("===== MENU FILE HANDLING =====")
print("1. Write (Tambah Buku)")
print("2. Read (Baca Buku)")
print("3. Write and Read")
print("4. Delete (Hapus Buku)")

pilihan = input("Pilih (1/2/3/4): ")

if pilihan == "1":
    buku = input("Masukkan nama buku: ")

    with open(nama_file, "a", encoding="utf-8") as file:
        file.write(buku + "\n")

    print("Nama buku berhasil disimpan!")

elif pilihan == "2":
    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            print("\n===== DAFTAR NAMA BUKU =====")
            isi = file.read()

            if isi:
                print(isi)
            else:
                print("Daftar buku masih kosong.")

    except FileNotFoundError:
        print("File daftar_buku.txt belum ditemukan.")

elif pilihan == "3":
    buku = input("Masukkan nama buku: ")

    with open(nama_file, "a", encoding="utf-8") as file:
        file.write(buku + "\n")

    with open(nama_file, "r", encoding="utf-8") as file:
        print("\n===== DAFTAR NAMA BUKU TERBARU =====")
        print(file.read())

elif pilihan == "4":
    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            daftar_buku = file.readlines()

        print("\n===== DAFTAR NAMA BUKU =====")
        for buku in daftar_buku:
            print(buku.strip())

        hapus_buku = input(
            "\nMasukkan nama buku yang ingin dihapus: "
        )

        daftar_baru = [
            buku for buku in daftar_buku
            if buku.strip().lower() != hapus_buku.strip().lower()
        ]

        if len(daftar_baru) == len(daftar_buku):
            print("Buku tidak ditemukan!")
        else:
            with open(nama_file, "w", encoding="utf-8") as file:
                file.writelines(daftar_baru)

            print("Buku berhasil dihapus!")

    except FileNotFoundError:
        print("File daftar_buku.txt belum ditemukan.")

else:
    print("Pilihan tidak valid!")
