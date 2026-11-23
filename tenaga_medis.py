class TenagaMedis:
    def __init__(self, id_staf, nama, shift):
        self.__id_staf = id_staf
        self.__nama = nama
        self.__shift = ""
        if not self.ubah_shift(shift):
            raise ValueError("Shift tidak valid")

    def get_id_staf(self):
        return self.__id_staf

    def get_nama(self):
        return self.__nama

    def get_shift(self):
        return self.__shift

    def ubah_shift(self, shift_baru):
        if shift_baru not in ("Pagi", "Siang", "Malam"):
            return False
        self.__shift = shift_baru
        return True

    def info(self):
        return f"[{self.__id_staf}] {self.__nama} | Shift {self.__shift}"
