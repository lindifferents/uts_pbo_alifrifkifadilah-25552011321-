from tenaga_medis import *

class Perawat(TenagaMedis):
    def __init__(self, id_staf, nama, shift, ruangan):
        super().__init__(id_staf, nama, shift)
        self.__ruangan = ruangan
        self.__jumlah_tugas = 0

    def get_ruangan(self):
        return self.__ruangan

    def get_jumlah_tugas(self):
        return self.__jumlah_tugas

    def pindah_ruangan(self, ruangan_baru):
        if ruangan_baru.strip() == "":
            return False
        self.__ruangan = ruangan_baru
        return True

    def selesaikan_tugas(self):
        self.__jumlah_tugas += 1
        return self.__jumlah_tugas

    def info(self):
        return super().info() + f" | Perawat Ruangan {self.__ruangan}"