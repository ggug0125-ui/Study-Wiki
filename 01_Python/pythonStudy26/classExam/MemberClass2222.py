
# 강사님 코드
# 클래스를 이용한 회원가입 코드다!!!!



import os
# MemberManager
#  ├─ file_name 변수
#  ├─ members
#  ├─ session
#  ├─ load_members() 메서드
#  ├─ save_members()
#  ├─ member_add()
#  ├─ member_login()
#  ├─ member_admin()
#  ├─ member_logout()
#  ├─ member_modify()
#  ├─ member_delete()
#  ├─ main_menu()
#  └─ run()

class MemberManager:
    def __init__(self, file_name="members.txt"):
        self.file_name = file_name
        self.members = []
        self.session = None
        self.load_members()

    # ===============================
    # 파일 로드
    # ===============================
    def load_members(self):
        self.members = [] #

        if not os.path.exists(self.file_name):
            self.save_members()
            return

        with open(self.file_name, "r", encoding="utf-8") as f:
            for line in f:
                data = line.strip().split("|")
                data[4] = True if data[4] == "True" else False
                self.members.append(data)

    # ===============================
    # 파일 저장
    # ===============================
    def save_members(self):
        with open(self.file_name, "w", encoding="utf-8") as f:
            for m in self.members:
                f.write(f"{m[0]}|{m[1]}|{m[2]}|{m[3]}|{m[4]}\n")

    # ===============================
    # 회원가입
    # ===============================
    def member_add(self):
        print("\n[회원가입]")
        uid = input("아이디 : ")

        for m in self.members:
            if m[0] == uid:
                print("이미 존재하는 아이디입니다.")
                return

        pw = input("비밀번호 : ")
        name = input("이름 : ")

        print("1.admin  2.manager  3.user")
        r = input("권한 선택 : ")

        role = "user"
        if r == "1":
            role = "admin"
        elif r == "2":
            role = "manager"

        self.members.append([uid, pw, name, role, True])
        self.save_members()
        print("회원가입 완료")

    # ===============================
    # 로그인
    # ===============================
    def member_login(self):
        print("\n[로그인]")
        uid = input("아이디 : ")
        pw = input("비밀번호 : ")

        for i, m in enumerate(self.members):
            if m[0] == uid:
                if not m[4]:
                    print("비활성화된 계정입니다.")
                    return

                if m[1] == pw:
                    self.session = i
                    print(f"{m[2]}님 로그인 성공 ({m[3]})")

                    if m[3] == "admin":
                        self.member_admin()
                    return
                else:
                    print("비밀번호 오류")
                    return

        print("존재하지 않는 아이디")

    # ===============================
    # 관리자 기능
    # ===============================
    def member_admin(self):
        print("\n[관리자 메뉴]")
        print("1. 비밀번호 변경")
        print("2. 블랙리스트")
        print("3. 권한 변경")
        print("0. 종료")

        sel = input("선택 : ")
        uid = input("대상 아이디 : ")

        for m in self.members:
            if m[0] == uid:
                if sel == "1":
                    m[1] = input("새 비밀번호 : ")
                elif sel == "2":
                    m[4] = False
                elif sel == "3":
                    m[3] = input("admin / manager / user : ")

                self.save_members()
                print("관리자 작업 완료")
                return

        print("대상 회원 없음")

    # ===============================
    # 로그아웃
    # ===============================
    def member_logout(self):
        self.session = None
        print("로그아웃 완료")

    # ===============================
    # 내정보 수정
    # ===============================
    def member_modify(self):
        if self.session is None:
            print("로그인 필요")
            return

        print("\n[내 정보 수정]")
        print("1. 이름 변경")
        print("2. 비밀번호 변경")

        sel = input("선택 : ")

        if sel == "1":
            self.members[self.session][2] = input("새 이름 : ")
        elif sel == "2":
            self.members[self.session][1] = input("새 비밀번호 : ")

        self.save_members()
        print("수정 완료")

    # ===============================
    # 회원탈퇴
    # ===============================
    def member_delete(self):
        if self.session is None:
            print("로그인 필요")
            return

        print("\n[회원 탈퇴]")
        print("1. 완전 탈퇴")
        print("2. 계정 비활성화")

        sel = input("선택 : ")

        if sel == "1":
            self.members.pop(self.session)
        elif sel == "2":
            self.members[self.session][4] = False

        self.session = None
        self.save_members()
        print("처리 완료")

    # ===============================
    # 메뉴
    # ===============================
    def main_menu(self):
        print("""
==== 회원관리 프로그램 (Class 기반) ====
1. 회원가입
2. 로그인
3. 로그아웃
4. 회원정보수정
5. 회원탈퇴
9. 종료
""")

    # ===============================
    # 실행
    # ===============================
    def run(self):
        while True:
            self.main_menu()
            sel = input(">>> ")

            if sel == "1":
                self.member_add()
            elif sel == "2":
                self.member_login()
            elif sel == "3":
                self.member_logout()
            elif sel == "4":
                self.member_modify()
            elif sel == "5":
                self.member_delete()
            elif sel == "9": break


# ===============================
# 프로그램 시작
# ===============================
app = MemberManager()
app.run()
