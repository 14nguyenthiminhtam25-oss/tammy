class Student:
    def __init__(self, name, math, literature, english):
        self.name = name
        self.scores = {"toán": math, "N văn": literature, "T anh": english}

    def avg(self):
        return sum(self.scores.values()) / 3

    def rank(self):
        a = self.avg()
        if a >= 9: return "xuất sắc"
        if a >= 8: return "giỏi"
        if a >= 5.5: return "khá"
        if a >= 4: return "trung bình"
        return "yếu"

    def show(self):
        print(f"tên: {self.name}")
        print("điểm:", self.scores)
        print("điểm tb:", round(self.avg(), 2))
        print("xếp loại:", self.rank())

    @classmethod
    def from_string(cls, data):
        name, m, v, e = data.split(",")
        return cls(name.strip(), float(m), float(v), float(e))

    @staticmethod
    def info():
        return "Lớp Student dùng để quản lý điểm học sinh."


# =========================
# VÍ DỤ — BẠN TAMMY
# =========================

tammy_data = "Tammy, 9, 7.5, 8"
tammy = Student.from_string(tammy_data)

tammy.show()
