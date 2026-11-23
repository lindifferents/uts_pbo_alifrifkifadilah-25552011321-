from tenaga_medis import *
from dokter import *
from perawat import *
from pasien import *

daftar_tenaga = []
daftar_pasien = []

daftar_tenaga.append(Dokter("D01", "Budi", "Pagi", "Umum", 50000))
daftar_tenaga.append(Dokter("D02", "Sari", "Siang", "Anak", 75000))
daftar_tenaga.append(Perawat("P01", "Rina", "Malam", "Ruang A"))
daftar_tenaga.append(Perawat("P02", "Dewi", "Pagi", "Ruang B"))
daftar_pasien.append(Pasien("PS1", "Ani", "Demam"))
daftar_pasien.append(Pasien("PS2", "Joko", "Batuk"))

daftar_tenaga[0].periksa_pasien(daftar_pasien[0])

def cari_tenaga(id_staf):
    for t in daftar_tenaga:
        if t.get_id_staf() == id_staf:
            return t
    return None

def cari_pasien(id_pasien):
    for p in daftar_pasien:
        if p.get_id_pasien() == id_pasien:
            return p
    return None

def tambah_data():
    print("\n1. Tambah Dokter\n2. Tambah Perawat\n3. Tambah Pasien")
    pilih = input("Pilih: ")
    try:
        if pilih in ("1", "2"):
            id_staf = input("ID Staf : ")
            if cari_tenaga(id_staf):
                print("ID sudah dipakai!")
                return
            nama = input("Nama    : ")
            shift = input("Shift (Pagi/Siang/Malam): ")
            if pilih == "1":
                spes = input("Spesialisasi: ")
                tarif = int(input("Tarif   : "))
                daftar_tenaga.append(Dokter(id_staf, nama, shift, spes, tarif))
            else:
                ruangan = input("Ruangan : ")
                daftar_tenaga.append(Perawat(id_staf, nama, shift, ruangan))
            print("Tenaga medis berhasil ditambahkan.")
        elif pilih == "3":
            id_p = input("ID Pasien: ")
            if cari_pasien(id_p):
                print("ID sudah dipakai!")
                return
            nama = input("Nama     : ")
            keluhan = input("Keluhan  : ")
            daftar_pasien.append(Pasien(id_p, nama, keluhan))
            print("Pasien berhasil ditambahkan.")
        else:
            print("Pilihan tidak valid.")
    except ValueError as e:
        print("Gagal:", e)

def tampilkan_data():
    print("\n=== TENAGA MEDIS ===")
    if not daftar_tenaga:
        print("(kosong)")
    for t in daftar_tenaga:
        print(t.info())
        if isinstance(t, Dokter):
            for p in t.get_daftar_pasien():
                print("    memeriksa ->", p.get_nama())
    print("\n=== PASIEN ===")
    if not daftar_pasien:
        print("(kosong)")
    for p in daftar_pasien:
        print(p.info())

def cari_data():
    print("\n1. Cari Tenaga Medis (ID)\n2. Cari Pasien (ID)")
    pilih = input("Pilih: ")
    if pilih == "1":
        t = cari_tenaga(input("ID Staf: "))
        print(t.info() if t else "Data tidak ditemukan.")
    elif pilih == "2":
        p = cari_pasien(input("ID Pasien: "))
        print(p.info() if p else "Data tidak ditemukan.")
    else:
        print("Pilihan tidak valid.")

def ubah_data():
    print("\n1. Ubah shift tenaga medis\n2. Ubah keluhan pasien"
          "\n3. Dokter memeriksa pasien")
    pilih = input("Pilih: ")
    if pilih == "1":
        t = cari_tenaga(input("ID Staf: "))
        if t is None:
            print("Data tidak ditemukan.")
            return
        print("Berhasil." if t.ubah_shift(input("Shift baru (Pagi/Siang/Malam): "))
              else "Shift tidak valid.")
    elif pilih == "2":
        p = cari_pasien(input("ID Pasien: "))
        if p is None:
            print("Data tidak ditemukan.")
            return
        print("Berhasil." if p.ubah_keluhan(input("Keluhan baru: "))
              else "Keluhan tidak boleh kosong.")
    elif pilih == "3":
        d = cari_tenaga(input("ID Dokter: "))
        p = cari_pasien(input("ID Pasien: "))
        if not isinstance(d, Dokter) or p is None:
            print("Dokter/Pasien tidak ditemukan.")
            return
        # Association: dokter memeriksa pasien
        print("Pemeriksaan berhasil." if d.periksa_pasien(p)
              else "Pasien sudah pernah diperiksa dokter ini.")
    else:
        print("Pilihan tidak valid.")

def cek_status():
    print("\n1. Status pasien\n2. Jumlah pasien yang diperiksa dokter")
    pilih = input("Pilih: ")
    if pilih == "1":
        p = cari_pasien(input("ID Pasien: "))
        print(f"Status {p.get_nama()}: {p.get_status()}" if p
              else "Data tidak ditemukan.")
    elif pilih == "2":
        d = cari_tenaga(input("ID Dokter: "))
        if isinstance(d, Dokter):
            print(f"Dr. {d.get_nama()} sudah memeriksa {d.jumlah_pasien()} pasien.")
        else:
            print("Dokter tidak ditemukan.")
    else:
        print("Pilihan tidak valid.")

def main():
    while True:
        print("\n===== APLIKASI KLINIK SEDERHANA =====")
        print("1. Tambah data\n2. Tampilkan data\n3. Cari data")
        print("4. Ubah data\n5. Cek status data\n6. Keluar")
        pilih = input("Pilih menu: ")
        if pilih == "1":
            tambah_data()
        elif pilih == "2":
            tampilkan_data()
        elif pilih == "3":
            cari_data()
        elif pilih == "4":
            ubah_data()
        elif pilih == "5":
            cek_status()
        elif pilih == "6":
            print("Terima kasih.")
            break
        else:
            print("Menu tidak valid.")

main()
