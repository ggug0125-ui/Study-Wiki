
class Score:           # 초기값
    def __init__(self, uid , kor, eng, math):
        self.uid = uid
        self.kor = kor
        self.eng = eng
        self.math = math

    @property
    def total(self):     # 합계
        return self.kor + self.eng + self.math

    def avg(self):       # 평균
        return round(self.total / 3, 2)   # 반올림 처리 정수 실수!!!

    @property
    def grade(self):
        if self.avg() >= 90:
            return "A"
        elif self.avg() >= 80:
            return "B"
        elif self.avg() >= 70:
            return "C"
        else:
            return "F"

    def to_line(self):     # 메모장 저장용
        return f"{self.uid}|{self.kor}|{self.eng}|{self.math}\n"

    @classmethod
    def from_line(cls, line):   # 메모장 리스트 객체화
        uid, kor, eng, math = line.strip().split("|")
        return cls(uid, int(kor), int(eng), int(math))
