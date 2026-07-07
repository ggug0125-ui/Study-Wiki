import os
from TestExam2.commom import Session
from TestExam2.domain import *

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "..", "data", "member.txt")

class MemberService:
    members = []

    @classmethod
    def load(cls):
        cls.members = []
        if not os.path.exists(FILE_PATH):
            cls.save()
            return
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            for line in f:
                member = Member.from_line(line)
                if member:
                    cls.members.append(member)

    @classmethod
    def save(cls):
        with open(FILE_PATH,"w",encoding="utf-8") as f:
            for m in cls.members:
                f.write(m.to_line() + "\n")

    @classmethod
    def signup(cls):
        print("\n[ 회 원 가 입 ]")
        uid = input("아이디 : ")
        if any(m.uid == uid for m in cls.members):
            print("이미 존재하는 아이디입니다.")
            return
        pw = input("비밀번호 : ")
        name = input("이름 : ")
        member = Member(uid,pw,name)
        print("회원가입 정보를 확인합니다.")
        print(f"아이디 : {member.uid}, 이름 : {member.name}")
        print(f"권한은 {member.role} 입니다.")
        save_True = input("회원가입하시려면 y를 누르세요 : ")
        if save_True == "y":
            cls.members.append(member)
            cls.save()
            print("회원가입이 완료되었습니다.")

    @classmethod
    def login(cls):
        print("\n[ 로 그 인 ]")
        uid = input("아이디 : ")
        pw = input("비밀번호 : ")
        for m in cls.members:
            if m.uid == uid:
                if not m.active:
                    print("비활성화된 계정입니다.")
                    return
                if m.pw == pw:
                    Session.login(m)
                    print(f"{m.name}님 로그인되었습니다.")
                    print(f"권한은 {m.role} 입니다.")
                    return
                else:
                    print("비밀번호가 틀렸습니다.")
                    return
        print("존재하지 않는 아이디입니다.")

    @classmethod
    def logout(cls):
        if not Session.is_login():
            print("로그인 후 이용하세요!!")
            return

        Session.logout()
        print("로그아웃 되었습니다.")


    @classmethod
    def my_modify(cls):
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
    def delete(cls):
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
    def admin_menu(cls):
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
    def list_member(cls):
        print("\n[ 회 원 목 록 ]")
        for m in cls.members:
            print(m)

    @classmethod
    def change_role(cls):
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
    def block_member(cls):
        uid = input("대상 아이디: ")
        for m in cls.members:
            if m.uid == uid:
                m.active = False
                cls.save()
                print("블랙리스트 처리 완료")
                return
        print("회원 없음")






