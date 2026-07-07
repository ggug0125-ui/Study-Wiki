import os
class MemberService:
    def __init__(self,FILE_NAME="member.txt"):           # 생성자
        self.FILE_NAME = FILE_NAME
        self.members = []
        self.session = None
        self.load_members()

    def load_members(self):                              # 자료 불러오기
        self.members = []
        if not os.path.exists(self.FILE_NAME):
            self.save_members()
            return
        with open(self.FILE_NAME,"r",encoding="utf-8") as f:
            for line in f:
                data = line.strip().split("|")
                data[4] = True if data[4] == "True" else False
                self.members.append(data)

    def save_members(self):                             # 자료 저장하기
        with open(self.FILE_NAME,"w",encoding="utf-8") as f:
            for m in self.members:
                f.write(f"{m[0]}|{m[1]}|{m[2]}|{m[3]}|{m[4]}\n")

    def member_add(self):                               # 회원가입
        print("회원 가입을 진행합니다.")
        uid = input("아이디를 입력하세요 : ")
        for m in self.members:
            if m[0] == uid:
                print("이미 존재하는 아이디입니다.")
                return
        pw = input("사용하실 비밀번호를 입력하세요 : ")
        name = input("사용자의 이름을 입력하세요 : ")
        role = "user"
        print(" 입력된 정보를 확인합니다. ")
        print("-" * 50)
        print(f"아이디 : {uid}   이름 : {name}")
        print(f"비민번호 : {pw}  권한 : {role}")
        print("-" * 50)
        save_True = input("회원가입하시려면 y를 누르세요 : ")
        if save_True == "y":
            self.members.append([uid,pw,name,role,True])
            self.save_members()
            self.load_members()
            print("회원 가입이 완료 되었습니다.")

    def member_login(self):                             # 회원 로그인
        print("\n로그인을 시작합니다.")
        uid = input("아이디: ")
        pw = input("비밀번호: ")
        for idx, m in enumerate(self.members):
            if m[0] == uid:
                if not m[4]:
                    print("비활성화된 계정입니다.")
                    return
                if m[1] == pw:
                    self.session = idx
                    print(f"{m[2]}님 환영합니다.")
                    print(f"{m[3]}권한으로 로그인이 되었습니다.")
                    if m[3] == "admin":
                        self.m_admin()
                    else:
                        self.subrun()
                    return
                else:
                    print("비밀번호가 틀립니다. 초기메뉴로 돌아갑니다.")
                    return
        else:
            print("존재하지 않는 아이디입니다.")
            return
    def my_data(self):                               # 내정보 보기
        print(f"아이디 : {self.members[self.session][0]}")
        print(f"이름 : {self.members[self.session][2]}")
        print(f"권한 : {self.members[self.session][3]} 입니다. ")

    def my_modify(self):                             # 내정보 수정
        self.my_data()
        print("1.아이디 변경 2.비밀번호 변경 3.이름변경")
        sel = input("선택번호 입력 : ")
        if sel == "1":
            new_id = input("변경할 아이디 : ")
            for m in self.members:
                if m[0] == new_id:
                    print("이미 존재하는 아이디입니다.")
                    return
            self.members[self.session][0] = new_id
            print(f"{new_id}으로 변경되었습니다.")

        elif sel == "2":
            self.members[self.session][1] = input("변경할 비밀번호: ")
            print(f"{self.members[self.session][1]}으로 변경되었습니다.")
        elif sel == "3":
            self.members[self.session][2] = input("변경할 이름: ")
            print(f"{self.members[self.session][2]}으로 변경되었습니다.")
        else:
            print("잘못된 번호입니다.")
            return
        self.save_members()
        self.load_members()

    def member_logout(self):                         # 로그아웃
        self.session = None
        print("로그아웃 되었습니다.")

    def main(self):                                  # 메인 메뉴
        print("""
=========== 회원 관리 서비스 ===========
1. 회원가입   2. 로그인   3. 프로그램종료
        """)

    def sub_main(self):                              # 로그인 화면 메뉴
        print("""
=== 회원관리 서비스에 오신걸 환영합니다 ===
1. 내 정보 보기  2. 내 정보 수정  3. 로그아웃 
4. 종료
        """)

    def m_admin(self):                               # 관리자 로그인 메뉴
        while True:
            print("""
============ 관 리 자 메 뉴 =============
1. 회원 전체 보기 
2. 권한 변경(회원 목록표시)
3. 블랙리스트 설정 (회원 목록표시) 
0. 종료
            """)
            sel = input("선택번호 : ")
            if sel == "1":
                self.a_list()
            elif sel == "2":
                self.a_list()
                uid = input("권한변경할 아이디: ")
                for m in self.members:
                    if m[0] == uid:
                        print("1.admin 2.manager 3.user")
                        role = input("변경할 번호 : ")
                        if role == "1":
                            m[3] = "admin"
                        elif role == "2":
                            m[3] = "manager"
                        elif role == "3":
                            m[3] = "user"
                        else:
                            print("잘못된 선택입니다.")
                            break
                        print("권한이 변경되었습니다.")
                        self.save_members()
                        self.load_members()

                        break
                else:
                    print("회원이 존재하지 않습니다.")
            elif sel == "3":
                self.a_list()
                uid = input("블랙리스트 처리할 아이디:")
                if self.members[self.session][0] == uid:
                    print("본인은 블랙리스트 처리할 수 없습니다.")
                    continue
                for m in self.members:
                    if m[0] == uid:
                        m[4] = False
                        print("블랙리스트 처리완료하였습니다.")
                        self.save_members()
                        self.load_members()
                        break
                else:
                    print("회원이 존재하지 않습니다.")
            elif sel == "0":
                print("관리자 메뉴를 종료합니다.")
                return

    def a_list(self):                                # 관리자전용 회원 목록
        print("\n 회원 목록")
        print("-" * 60)
        print(f"{'ID':10} {'이름':10} {'권한':10} {'상태':10}")
        print("-" * 60)
        for m in self.members:
            status = "활성화" if m[4] else "비활성화"
            print(f"{m[0]:10} {m[2]:10} {m[3]:10} {status:10}")
            print("-" * 60)

    def run(self):                                    # 주 실행 코드
        while True:
            self.main()
            select = input("선텍번호 입력 : ")
            if select == "1": self.member_add()
            elif select == "2": self.member_login()
            elif select == "3": break

    def subrun(self):                                 # 부 실행코드
        while True:
            self.sub_main()
            sel = input("선택번호 입력 : ")
            if sel == "1": self.my_data()
            elif sel == "2": self.my_modify()
            elif sel == "3": self.member_logout()
            elif sel == "4": break

app = MemberService()
app.run()