class Student:
    def __init__(self, name, math, literature, english, school, classroom, address):
        self.name = name
        self.scores = {"Toán": math, "Văn": literature, "Anh": english}
        self.school = school       
        self.classroom = classroom 
        self.address = address     

    def avg(self):
        return sum(self.scores.values()) / 3

    def rank(self):
        a = self.avg()
        if a >= 9: return "Xuất sắc"
        if a >= 8: return "Giỏi"
        if a >= 6.5: return "Khá"
        if a >= 5: return "Trung bình"
        return "Yếu"

    def best_subject(self):
        subject = max(self.scores, key=self.scores.get)
        score = self.scores[subject]
        return subject, score

    def show(self):
        print(f"Tên: {self.name}")
        print("Trường:", self.school)
        print("Lớp:", self.classroom)
        print("Địa chỉ:", self.address)
        print("Điểm:", self.scores)
        print("Điểm TB:", round(self.avg(), 2))
        print("Xếp loại:", self.rank())
        mon, diem = self.best_subject()
        print(f"Môn cao nhất: {mon} ({diem})")

    @classmethod
    def from_string(cls, data):
        name, m, v, e, school, classroom, address = data.split(",")
        return cls(name.strip(), float(m), float(v), float(e),
                   school.strip(), classroom.strip(), address.strip())

    @staticmethod
    def info():
        return "Lớp Student mở rộng để quản lý học sinh đầy đủ."


tammy_data = "Tammy, 9, 7.5, 8, THCS VÕ TRƯỜNG TOẢN, 6/2, Q1"
tammy = Student.from_string(tammy_data)

tammy.show()
