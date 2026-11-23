class Pasien:
    def __init__(self, id_pasien, nama, keluhan):
        self.__id_pasien = id_pasien
        self.__nama = nama
        self.__keluhan = keluhan
        self.__status = "Menunggu"
        self.__dokter = None

    def get_id_pasien(self):
        return self.__id_pasien

    def get_nama(self):
        return self.__nama

    def get_keluhan(self):
        return self.__keluhan

    def get_status(self):
        return self.__status

    def get_dokter(self):
        return self.__dokter

    def ubah_keluhan(self, keluhan_baru):
        if keluhan_baru.strip() == "":
            return False
        self.__keluhan = keluhan_baru
        return True

    def ubah_status(self, status_baru):
        if status_baru not in ("Menunggu", "Sudah Diperiksa"):
            return False
        self.__status = status_baru
        return True

    def set_dokter(self, dokter):
        self.__dokter = dokter

    def info(self):
        nama_dokter = self.__dokter.get_nama() if self.__dokter else "-"
        return (f"[{self.__id_pasien}] {self.__nama} | Keluhan: {self.__keluhan}"
                f" | Status: {self.__status} | Dokter: {nama_dokter}")