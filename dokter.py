from tenaga_medis import *

class Dokter(TenagaMedis):
    def __init__(self, id_staf, nama, shift, spesialisasi, tarif):
        super().__init__(id_staf, nama, shift)
        if tarif < 0:
            raise ValueError("Tarif tidak valid")
        self.__spesialisasi = spesialisasi
        self.__tarif = tarif
        self.__daftar_pasien = []

    def get_spesialisasi(self):
        return self.__spesialisasi

    def get_tarif(self):
        return self.__tarif

    def get_daftar_pasien(self):
        return self.__daftar_pasien

    def periksa_pasien(self, pasien):
        if pasien in self.__daftar_pasien:
            return False
        self.__daftar_pasien.append(pasien)
        pasien.set_dokter(self)
        pasien.ubah_status("Sudah Diperiksa")
        return True

    def jumlah_pasien(self):
        return len(self.__daftar_pasien)

    def info(self):
        return (super().info() +
                f" | Dokter {self.__spesialisasi} | Tarif Rp{self.__tarif}")