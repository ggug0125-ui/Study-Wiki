import os

from Member import Member

class MemberService:  #객체의 CRUD를 넣는다
    def __init__(self,file_name="member.txt"):
        self.file_name = file_name
        self.member = None
        self.members = []
        self.session = None
        self.load_members()

    def run(self):
        run = True
        while run:
            self.main_menu()
            sel = input(">>>")
            if sel == "1": self.member_add()
            elif sel == "2": self.member_login()
            elif sel == "3": self.member_logout()
            elif sel == "4": self.member_modify()
            elif sel == "5": self.member_delete()
            elif sel == "9": run = False
            else:
                print("잘못 입력하셨습니다.")

    def save_members(self):        # 저장 메서드
        with open(self.file_name,"w",encoding="utf-8") as f:
            for member in self.members:
                f.write(member.to_line())


    def load_members(self):        # 읽기 메서드
        if not os.path.exists(self.file_name):
            self.save_members()
            return
        self.members = [] # 메모리에 남은 값을 초기화
        with open(self.file_name,"r",encoding="utf-8") as f:
            for line in f:
                self.members.append(Member.from_line(line))


    def find_member(self,uid):
        for member in self.members:
            if member.id == uid:
                print(member.name,"님을 찾았습니다.")
                return member
        return None



    def main_menu(self):
        print("""
====회원 관리프로그램(Member 객체 기반 ver 1)====
1. 회원가입
2. 로그인
3. 로그아웃
4. 회원정보수정
5. 회원탈퇴
9. 종료
        """)

    def admin_menu(self):
        print("""
----- [ 관리자 메뉴 ] -----
1. 회원리스트 조회
2. 비밀번호 변경
3. 블랙리스트 처리
4. 권한 변경
9. 종료
        """)

    def member_add(self):
        print("\n [회원가입] ")
        uid = input("아이디 : ")
        if self.find_member(uid):
            print("이미 존재하는 아이디입니다.")
            return
        pw = input("비밀번호 : ")
        name = input("이름 : ")
        role = "user"
        self.members.append(Member(uid,pw,name,role))
        self.save_members()
        self.load_members()
        print("회원가입이 완료 되었습니다.")


    def member_admin(self):
        subrun = True
        while subrun:
            self.admin_menu()
            sel = input("선택: ")
            if sel == "1":
                print("***회원 리스트 조회***")
                self.show_member_list()
            elif sel == "2":
                print("비밀번호 변경")
                uid = input("대상 아이디 : ")
                member = self.find_member(uid)
                if member:
                    member.pw = input("새 비밀번호 : ")
                    self.save_members()
                    self.load_members()
                    print("비밀번호 변경 완료")
                else:
                    print("변경할 회원이 없습니다.")
            elif sel == "3":
                print("블랙리스트 처리")
                uid = input("대상 아이디 : ")
                member = self.find_member(uid)
                if member:
                    member.active = False
                    self.save_members()
                    self.load_members()
                    print("블랙리스트 처리 완료되었습니다.")
                else:
                    print("변경할 회원이 없습니다.")
            elif sel == "4":
                print("---권한 변경---")
                uid = input("대상 아이디 : ")
                member = self.find_member(uid)
                print("=====권한 변경=====")
                print("1.admin  2. manager  3. user ")
                sel = input(">>>")
                if sel == "1":
                    member.role = "admin"
                    self.save_members()
                    self.load_members()
                elif sel == "2":
                    member.role = "manager"
                    self.save_members()
                    self.load_members()
                elif sel == "3":
                    member.role = "user"
                    self.save_members()
                    self.load_members()
                else:
                    print("잘못입력하셨습니다.")

            elif sel == "9":
                print("관리자 메뉴를 종료합니다.")
                subrun = False





    def member_login(self):
        print("로그인 메뉴입니다.")
        uid = input ("아이디 : ")
        pw = input("비밀번호 : ")
        member = self.find_member(uid)
        if not member:
            print("존재하지 않는 아이디 입니다.")
            return
        if member.pw == pw:
            self.session = member
            print(f"{member.name}님 로그인성공")
            print(f"권한은 {member.role} 입니다. ")
            if member.role == "admin":
                self.member_admin()
        else:
            print("비밀번호가 틀렸습니다.")

    def member_logout(self):
        sel = input("로그아웃을 진행하시겠습니까? y/n : ")
        if sel == "y":
            self.session = None
            print("로그아웃 되었습니다.")
        else:
            print("로그아웃이 취소 되었습니다.")
            return

    def show_member_list(self):
        print("\n[ 회 원 목 록 ]")
        print("-" * 60)
        print(f"{'아이디':10}{'이름':10}{'권한':10}{'상태':10}")
        print("-" * 60)
        for member in self.members:
            status = "활성" if member.active else "비활성"
            print(f"{member.id:10}{member.name:10}{member.role:10}{status:10}")
        print("-" * 60)


    def member_modify(self):
        if not self.session:
            print("로그인이 필요합니다.")
            self.member_login()
            return
        print("1, 이름 변경")
        print("2. 비밀번호 변경")
        print("3. 아이디 변경")
        sel = input(">>> ")
        if sel == "1":
            self.session.name = input("새이름 : ")
            print(f"변경된 이름은 {self.session.name} 입니다.")
            self.save_members()
            self.load_members()
        elif sel == "2":
            self.session.pw = input("새비밀번호 : ")
            print(f"변경된 비밀번호는 {self.session.pw} 입니다.")
            self.save_members()
            self.load_members()
        elif sel == "3":
            self.session.uid = input("새 아이디 : ")
            print(f"변경된 아이디는 {self.session.uid} 입니다.")
            self.save_members()
            self.load_members()
        else:
            print("선택하신 번호가 없습니다.")
            return

    def member_delete(self):
        if not self.session:
            print("로그인이 필요합니다.")
            self.member_login()
            return

        sel = input("비밀번호 입력 : ")
        if sel == self.session.pw:
            print("회원을 탈퇴합니다..")
            self.members.remove(self.session)
            self.session = None
            print("회원 탈퇴 성공 ")
            self.save_members()
            self.load_members()
        else:
            print("비밀번호가 틀렸습니다.")
            return



