import os   # 텍스트 파일 처리용
from packageExam.LMS.commom import Session
from packageExam.LMS.domain import *

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "..", "data", "member.txt")

class MemberService:
    members = []

    @classmethod
    def load(cls):                          # 파일에서 읽어와
        cls.members = []

        if not os.path.exists(FILE_PATH):
            cls.save()
            return

        with open(FILE_PATH, "r", encoding="utf-8") as f:
            for line in f:
                member = Member.from_line(line)
                if member:  # ⭐ None이면 추가 안 함
                    cls.members.append(member)

    @classmethod
    def save(cls):                                 # 저장해~
        with open(FILE_PATH,"w",encoding="utf-8") as f:
            for m in cls.members:
                f.write(m.to_line() + "\n")  # 줄로 기록해라~!!!

    @classmethod
    def login(cls):                                # 로그인 해~
        print("\n[ 로 그 인 ]")
        uid = input("아이디 : ")
        pw = input("비밀번호 : ")
        for m in cls.members:
            if m.uid == uid:
                if not m.active:
                    print("비활성화된 계정입니다.")
                    return
                if m.pw == pw:
                    Session.login(m)     # 로그인 성공시 세션객체에 멤버를 넣음
                    print(f"{m.name}님 로그인 성공 ({m.role})")
                    print(m)
                    return
                else:
                    print("비밀번호가 틀렸습니다.")
                    return
        print("존재하지 않는 아이디입니다.")

    @classmethod
    def logout(cls):                                #로그아웃 헤~
        if not Session.is_login():
            print("로그인 상태가 아닙니다.")
            return

        Session.logout()  # session = None
        print("로그아웃 완료")

    @classmethod
    def signup(cls):                                # 회원 가입해~
        print("\n[ 회 원 가 입 ]")
        uid = input("아이디 : ")
        if any(m.uid == uid for m in cls.members):
            print("이미 존재하는 아이디입니다.")
            return
        pw = input("비밀번호 : ")
        name = input("")
        member = Member(uid, name, pw)
        cls.members.append(member)
        cls.save()
        print("회원가입 완료")

    @classmethod
    def modify(cls):                                # 회원 수정해~
        if not Session.is_login():
            print("로그인 상태가 아닙니다.")
            return
        member = Session.login_member
        print("""
    [ 내 정 보 수 정 ] 
    1. 이름 변경
    2. 비밀번호 변경
    0. 취소
    """)
        sel = input("선택 : ")
        if sel == "1":
            member.name = input("새 이름 : ")
        elif sel == "2":
            member.pw = input("새 비밀번호 : ")
        else:
            return
        cls.save()
        print("정보 수정이 완료되었습니다.")

    @classmethod
    def delete(cls):                                 # 회원 탈뢰 및 계정 비활성화~~
        if not Session.is_login():
            print("로그인 후 이용가능합니다.")
            return
        member = Session.login_member
        print("""
    [ 회 원 탈 퇴 ]
    1. 완전 탈퇴
    2. 계정 비활성화
    """)
        sel = input("선택 : ")
        if sel == "1":
            cls.members.remove(member)
            Session.logout()
            cls.save()
            print("회원 탈퇴 완료")
        elif sel == "2":
            member.active = False
            Session.logout()
            cls.save()
            print("계정 비활성화 완료")

    @classmethod
    def admin_menu(cls):                              # 관리자 용~~~~~~~~
        if not Session.is_login() or not Session.login_member.is_admin():
            print("관리자만 접근 가능합니다.")
            return
        while True:
            print("""
    [ 관 리 자 메 뉴 ]
    1. 회원 목록 조회
    2. 권한 변경
    3. 블랙리스트 처리
    0. 뒤로가기
    """)
            sel = input("선택 번호 : ")
            if sel == "1":
                cls.list_member()
            elif sel == "2":
                cls.change_role()
            elif sel == "3":
                cls.block_member()
            elif sel == "0":
                break

    @classmethod
    def list_member(cls):                              # 회원 보기용~~
        print("\n[ 회 원 목 록 ]")
        for m in cls.members:
            print(m)

    @classmethod
    def change_role(cls):                              # 권한 변경 ~~~~~~~
        uid = input("대상 아이디 : ")

        for m in cls.members:
            if m.uid == uid:
                print("""
[ 권 한 변 경 ]
1. 관리자(admin)
2. 매니저(manager)
3. 일반 사용자 (user)
""")
                sel  = input("선택 번호 : ")
                if sel == "1":
                    m.role = "admin"
                elif sel == "2":
                    m.role = "manager"
                elif sel == "3":
                    m.role = "user"
                else:
                    print("잘못된 선택입니다.")
                    return

                cls.save()
                print(" 권한 변경이 완료 되었습니다.")
                return
        print("회원 없음")

    @classmethod
    def block_member(cls):                                # 블랙리스트 변경~~~~~~~~
        uid = input("대상 아이디: ")
        for m in cls.members:
            if m.uid == uid:
                m.active = False
                cls.save()
                print("블랙리스트 처리 완료")
                return
        print("회원 없음")






