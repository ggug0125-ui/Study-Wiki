# Member 객체를 CRUD 기능을 넣는다
# 메뉴구현
# 텍스트 파일 처리 (파일 읽기, 파일 저장)
# 회원 가입, 로그인, 로그아웃, 회원 수정, 회원 탈퇴
import os

from Member import Member # 회원 객체 추가연결 멤버파일을 가져와~~~
# 사용법 member = Member() -> 객체가 생성됨
#       member. 필드/메서드 = ???

class MemberService:
    def __init__(self,file_name="member.txt"):
        # 클래스가 생성할때 초기값 관리
        self.member = None
        self.file_name = file_name
        self.members = []     # 회원들을 리스트로 만들어 Member()객체를 담는다
        self.session = None   # 로그인 상태를 담당(members의 인덱스 보관용)
        self.load_members()   # 아래쪽 메서드 호출
        # 처음 시작할때 변수를 만들어서 시작하는거야~

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
                print("잘못 입력 하셨습니다.")



    def load_members(self):  #파일에서 메로리로 불러온다
        if not os.path.exists(self.file_name): #맨위에 import os
            self.save_members()
            return
        self.members = []  #메모리에 남은 값을 초기화

        with open(self.file_name,"r",encoding="utf-8") as f:
            for line in f:
                self.members.append(Member.from_line(line))
                #                       line은 객체야 그전엔 리스트[][]요걸로 들어왔어
                #                   Member객체에 .form_line()메서드 실행
                #                                   1줄을 가져와 클래스로 만듬
                #   member리스트에 뒷부분에 추가


    def main_menu(self):
        print("""
===== 회원 관리 프로그램 (Member 객체 기반) =====
1. 회원가입
2. 로그인
3. 로그아웃
4. 회원정보수정
5. 회원탈퇴
9. 종료          
        """)

    def member_add(self):
        print("\n[회원가입]")
        uid = input("아이디 : ")

        if self.find_member(uid):  # 자주쓰는 중복코드로 메서드 처리함!!
            print("이미 존재하는 아이디입니다.")
            return

        pw = input("비밀번호 : ")
        name = input("이름 : ")
        role = "user"

        self.members.append(Member(uid,pw,name,role))
        # 대문자멤버클래스에 객체로 꽂았어!! init 초기값으로 들어감)
        self.save_members()
        self.load_members()
        print("회원 가입 완료")

    def member_login(self):
        print("\n[로그인]")
        uid = input("아이디 : ")
        pw = input("비밀번호 : ")

        member = self.find_member(uid)
        if not member:
            print("존재하지 않는 아이디")
            return
        if member.pw == pw:
            self.session = member
            print(f"{member.name}님 로그인 성공 ({member.role})")
            if member.role == "admin":
                self.member_admin() #관리자용 메서드 들어감
        else:
            print("비밀번호 오류")


    def member_logout(self):
        sel = input("로그아웃을 진행하시겠습니다까y/n : ")
        if sel == "y":
            self.session = None
            print("로그아웃 되었습니다.")

        else:
            print("로그아웃이 취소되었습니다.")
            return



    def member_modify(self):
        if not self.session:
            print("로그인이 필요합니다.")
            self.member_login()
            return
        print("1. 이름 변경 ")
        print("2. 비밀번호 변경 ")
        print("3. 아이디 변경 ")
        sel = input(">>> ")
        if sel == "1":
            self.session.name = input("새 이름 : ")
            print(f"변경된 이름은 : {self.session.name} 입니다.")
            self.save_members()
            self.load_members()
        elif sel == "2":
            self.session.pw = input("새 비밀번호 : ")
            print(f"변경된 비밀번호는 {self.session.pw}")
            self.save_members()
            self.load_members()
        elif sel == "3":
            self.session.uid = input("새 아이디 : ")
            print(f"변경된 아이디는 : {self.session.uid}")
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
            print("회원 탈퇴 성공 ")
            self.save_members()
            self.load_members()
        else:
            print("비밀번호가 틀렸습니다.")
            return




    # 파일 저장용 코드
    def save_members(self):
        with open(self.file_name, "w", encoding="utf-8") as f:
            for member in self.members:
                f.write(member.to_line())
                #  Member객체에 메서드를 사용하여 한줄씩 기록
                # Member 파일에서 가져오는거야~

    # 아이디를 이용해 members에서 찾는 공통 메서드
    def find_member(self, uid):
        for member in self.members:
        # 멤버스 리스트에서 1개씩 멤버를 가져와!!
            if member.id == uid: # 가져온 멤버객체.id와 전달받은 id가 같은지??
                print(member.name, "님을 찾았습니다. ")
                # 예전에는 member[2]번으로 찾았는데 지금은 변수명으로 찾을수있음

                return member    # 같은게 있으면 member 객체를 리턴
        return None              # None으로 리턴

    def member_admin(self):
        # role ="admin" 에 진입가능한 메서드
        subrun = True
        while subrun:
            print("\n[관리자 메뉴]")
            print("1. 회원 리스트 조회")
            print("2. 비밀번호 변경")
            print("3. 블랙리스트 처리")
            print("4. 권한 변경")
            print("9. 종료")
            sel = input("선택 : ")
            # 회원 목록 보기
            if sel == "1":
                print("--회원리스트 조회--")
                self.show_member_list()
            # 비밀번호 변경
            elif sel == "2":
                print("--비밀번호 변경--")
                uid = input("대상아이디 : ")
                member = self.find_member(uid)
                if member:
                    member.pw = input(" 새 비밀번호 : ")
                    self.save_members()
                    print("비밀번호 변경 완료")
                else:
                    print("회원 없음")
            elif sel == "3":
                print("--블랙리스트 처리--")
                uid = input("대상아이디 : ")
                member = self.find_member(uid)
                if member:
                    member.active = False
                    self.save_members()
                    print("블랙리스트 처리완료")
                else:
                    print("회원 없음")
            elif sel == "4":
                print("--권한 변경--")
                uid = input("대상아이디 : ")
                member = self.find_member(uid)
                if member:
                    member.role = input("admin/manager/user : ")
                    self.save_members()
                    print("권한 변경 완료")
                else:
                    print("회원 없음")

            elif sel == "9":
                print(" 관리자 메뉴를 종료 합니다. ")
                subrun = False


    def show_member_list(self):
        # 관리자가 볼수있는 회원 리스트
        print("\n[회원 목록]")
        print("-" * 60)
        print(f"{'아이디':10}{'이름':10}{'권한':10}{'상태'}")
        print("-"*60)
        for member in self.members: # 멤버스의 배열에서 하나씩 튀어나와
        # 멤버스 리스트에 있는 객체를 하나씩 가져와 멤버에 넣음
            status = "활성" if member.active else "비활성" # 문자열로 활성이나 비활성으로 보여줘!!!
            # member.active == True면 status변수에 "활성"을 넣고 아니면 "비활성"
            print(f"{member.id:10}{member.name:10}{member.role:10}{status}")
            #                                                          여긴 활성 비활성 글자가 들어가는거야!!
        print("-"*60)




