import os
from packageExam.LMS.domain import Score
from packageExam.LMS.commom import Session
from packageExam.LMS.service.BoardService import FILE_PATH

FILE_PATH = "data/score.txt"

class ScoreService(Session):
    scores = []

    @classmethod
    def load(cls):                                    # 읽어와
        cls.scores = []

        if not os.path.exists(FILE_PATH):
            cls.save()
            return

        with open(FILE_PATH, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:  # ⭐ 빈 줄 제거
                    continue

                score = Score.from_line(line)
                if score:
                    cls.scores.append(score)

    @classmethod
    def save(cls):  # 점수 저장
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            for s in cls.scores:
                if s is None:
                    continue
                f.write(s.to_line() + "\n")

    @classmethod
    def run(cls):                                      # 실행코드
        if Session.login_member is None:
            print("로그인 후 이용가능합니다.")
            return
        member = Session.login_member
        cls.load()                                    # 전제성적 불러오기
        while True:
            print("\n======성 적 관 리======")
            print("1. 내 성적 조회")
            if member.role in ("manager","admin"):
                print("2. 학생 성적 입력 / 수정")
                print("3. 전체 성적보기")
            print("0. 종료")

            sel = input("번호 입력 : ")
            if sel == "1":
                cls.view_my_score()
            elif sel == "2" and member.role in ("manager","admin"):
                cls.add_score()
            elif sel == "3" and member.role in ("manager", "admin"):
                cls.view_all()
            elif sel == "0":
                break

    @classmethod
    def add_score(cls):                                    # 성적 입력
        member = Session.login_member
        if member.role not in ("manager","admin"):
            print("성적 입력 권한이 없습니다.")
        uid = input("성적입력 학생 아이디 : ")
        cls.scores = [s for s in cls.scores if s.uid != uid]
        kor = int(input("국어 점수 : "))
        eng = int(input("영어 점수 : "))
        math = int(input("수학 점수 : "))
        cls.scores.append(Score(uid, kor, eng, math))
        cls.save()
        print("성적입력을 완료하였습니다.")

    @classmethod
    def view_my_score(cls):                                  # 내 성적보기
        member = Session.login_member
        for s in cls.scores:
            if s.uid == member.uid:
                cls.print_score(s)
                break
        print("등록된 성적이 없습니다.")

    @classmethod
    def view_all(cls):                                        # 전체성적보기
        member = Session.login_member
        if member.role != "admin" and member.role != "manager":
            print("접근권한이 없습니다.")
            return
        print("\n [ 전체 성적 목록 ] ")
        for s in cls.scores:
            cls.print_score(s)

    @staticmethod
    def print_score(s):                                        # 출력 공통 함수
        print(
            f"ID:{s.uid} | "
            f"국어:{s.kor} 영어:{s.eng} 수학:{s.math} | "
            f"총점:{s.total} 평균:{s.avg} | 등급 : {s.grade}"
        )

