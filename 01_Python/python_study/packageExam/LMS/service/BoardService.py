from packageExam.LMS.domain import Board       # 게시판 객체 가져와
from packageExam.LMS.commom import Session     # 로그인한 객체 가져와
import os

FILE_PATH = "data/board.txt"    # 데이타 파일안에 보드.txt파일 가져와

class BoardService:
    board = []

    @classmethod
    def load(cls):
        if not os.path.exists(FILE_PATH):
            return

        cls.boards = []

        with open(FILE_PATH, "r", encoding="utf-8") as f:
            for line in f:
                board = Board.from_line(line)
                if board:  # None이면 건너뜀
                    cls.boards.append(board)

    @classmethod
    def save(cls):             # 파일 저장
        with open(FILE_PATH,"w",encoding="utf-8") as f:
            for b in cls.boards:
                f.write(b.to_line() + "\n")

    @classmethod
    def write(cls):            # 게시글 작성
        if not Session.is_login():
            print("로그인 하세요~")
            return

        title = input("제목 : ")
        content = input("내용 : ")
        writer = Session.login_member.uid

        no = len(cls.boards) + 1
        cls.boards.append(Board(no, title, content, writer))
        cls.save()
        print("작성하신 글이 등록되었습니다.")

    @classmethod
    def list(cls):                             # 게시글 목록 보기
        print("\n[게시글 목록]")

        has_board = False

        for b in cls.boards:
            if b.active:
                print(f"{b.no} / {b.title} / {b.writer} / {b.content}")
                has_board = True

        if not has_board:
            print("등록된 게시글이 없습니다.")

    @classmethod
    def delete(cls):
        if not Session.is_login():
            print("로그인 후 이용하세요.")
            return
        no = int(input("삭제할 글 번호 : "))
        for b in cls.boards:
            if b.no == no:
                if (Session.login_member.uid == b.writer or
                        Session.login_member.role == "admin"):
                    b.active = False
                    cls.save()
                    print("삭제 되었습니다.")
                else:
                    print("권한이 없습니다.")
                return
        print("삭제할 글이 없습니다.")

    @classmethod
    def run(cls):
        cls.load()
        while True:
            print("""
    [ 게 시 판 ]
     1. 글쓰기
     2. 글목록
     3. 글삭제
     0. 뒤로가기
     """)
            sel = input("선택할 번호 : ")
            if sel == "1":
                cls.write()
            elif sel == "2":
                cls.list()
            elif sel == "3":
                cls.delete()
            elif sel == "0":
                break




