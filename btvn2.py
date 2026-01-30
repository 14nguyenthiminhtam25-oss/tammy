class HocSinh:

    so_luong = 0
    danh_sach_diem = []

    def __init__(self, ten, diem):
        self.ten = ten
        self.diem = diem

        HocSinh.so_luong += 1

        HocSinh.danh_sach_diem.append(diem)

    @staticmethod
    def dem_so_hoc_sinh():
        return HocSinh.so_luong

    @classmethod
    def tinh_diem_trung_binh(cls):
        if len(cls.danh_sach_diem) == 0:
            return 0
        return sum(cls.danh_sach_diem) / len(cls.danh_sach_diem)

hs1 = HocSinh("An", 8)
hs2 = HocSinh("Hùng", 10)
hs3 = HocSinh("Trang", 7)

print("Số học sinh:", HocSinh.dem_so_hoc_sinh())

print("Điểm trung bình:", HocSinh.tinh_diem_trung_binh())
