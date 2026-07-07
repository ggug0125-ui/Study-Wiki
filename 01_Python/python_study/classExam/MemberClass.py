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

class MemberManager:    #객체를 담당하는 클래스 사용법은 변수 = MemberManager() # 클래스 시작 초기값 설정
    # 클래스에서 self 는 객체의 주소를 가지고있음
    # def __init__(self) 클래스 구현시 필수
    def __init__(self,FILE_NAME="members.txt"):                # 생성자 초값을 가지고 있다
        self.FILE_NAME = FILE_NAME      # 파일을 가져와 접속한 사람마다 각자 파일네임을 쓰게하는것  객체에 파일이름을 넣는다
        self.members = []     # 이차원배열 # 객체에 멤버스 리스트를 만든다
        self.session = None   # 로그인 상태를 유지 # 객체에 세션변수를 만들고 기본값으로 None 처리(정수)
        self.load_member()    # 매서드 - 멤버스라는 리스트를 가져온다 # 아래에 선언된 load_member()메세드를 호출한다

    def load_member(self):    # 앞으로 만들 메서드()괄호안에 self가 필수     # 자료 불러오기
        self.members = []     # 빈배열로 생성 (혹시나, 이전에 리스트가 남아있을수있음
        if not os.path.exists(self.FILE_NAME):  #동일 디렉토리에 파일명이 없으면???
            self.save_members()   # save_members()매서드를 호출(open()으로 파일생성)
            return                  # load_member()매서드를 빠져나와라

        with open(self.FILE_NAME, "r" ,encoding ="utf-8") as f:     # 자료를 불러오려면 읽어아쟈~!!! "r" 은 읽는거야
            #    members.txt     읽기전용         한글처리 필수  -> f라는 변수에 넣어라
            for line in f:     # f변수에 있는 파일객체를 줄단위로 반복함
                data = line.strip().split("|")  # strip()  한줄읽은 값을 엔터제거  split("|") 기준으로 잘라->1차원 리스트로생성
                #["kkw","김기원","0000","admin","True"]
                data[4] = True if data[4] == "True" else False   #"True" 쌍따옴표제거 불타입 True로 변경 아니면 False
                self.members.append(data)
                # 2차원 배열인 members 맨뒤에 추가~~ for 종료까지
            print(self.members)

    def save_members(self):  #member 2차원 리스트값을 파일로 덮어써라    # 자료 저장하기 "W" 이거 꼭확인해!!! 쓰는거야!!
            # 왜??? 파일처리는 수정을 하지 않는다 r(일기전용), w(덮어쓰기), a(마지막에 추가)
        with open(self.FILE_NAME, "w", encoding="utf-8") as f:
            #        members.txt 덮어쓰기         한글처리  -> f 변수에 넣어라
            for m in self.members: # 메모리에 있는 member 2차원 리스트를 한줄씩 가져와서 m 변수에 넣어라
                #  m =    ["kkw","김기원","0000","admin","True"]
                f.write(f"{m[0]}|{m[1]}|{m[2]}|{m[3]}|{m[4]}\n")
                #            kkw|김기원|0000|admin|True 엔터  -> write 저장 -> for 종료시까지

    def member_add(self):      # self 는 클랫의 객체 주소                       # 회원가입
        print("회원 가입을 합니다.")
        uid = input(" 아이디 : ")  # 키보드로 입력한 값을 uid변수에 넣음
        for m in self.members:    # 2차원 배열인 member에 1차원 리스트를 가져와(1줄)
            if m[0] == uid:
                print("이미 존재하는 아이디입니다.")
                return   # member_add()를 빠져나옴  컨티뉴 를하면 for문으로 돌아가
        # 중복 id가 없으면 아래쪽 코드 실행 -> else: 로 처리해도 되나 -> 들여쓰기가 깊어져 선택이야
        pw = input(" 비밀번호: ")
        name  = input("이름 : ")
        print("1. admin   2. manager   3. user")
        roleselect = input("권한을 선택하세요 : ")

        role = "user"
        if roleselect == "1":
            role = "admin"
        elif roleselect == "2":
            role = "manager"
        print(" 입력된 정보를 확인합니다. " )
        print("-" * 50)
        print(f"아이디 : {uid}   이름 : {name}")
        print(f"비민번호 : {pw}  권한 : {role}")
        print("-" * 50)
        # 여기까지가 변수에 입력완료
        save_True = input("저장하려면 y를 누르세요 : ")
        if save_True == "y":
            self.members.append([uid, name, pw, role, True]) # 멤버스에 있는 2차원배열로 만들어저장 추가저장 append
            self.save_members() # 여기에 저장
            self.load_member() #저장했다 다시불러오기
            print("회원 가입이 완료 되었습니다.")


    def member_login(self):                                 # 로그인하기~!!!
        print("\n 로그인을 진헹합니다. ")
        uid = input("아이디 : ")
        pw = input("비밀번호 : ")
        # enumerate() 2차원 배열을 인덱스와 리스트를 추출한다
        for idx, m in enumerate(self.members):
        # idx는 인덱스, m은 멤버스
            if m[0] == uid: # for 문 중에 같으 아이디가 있으면
                if not m[4]: #active가 false 인지 확인
                    print("로그인을 할수 없습니다.(블랙리스트,비활성화)")
                    return  # member_login()종료
                if m[2] == pw:   # active가 True면
                    self.session = idx  # 로그인한 주소값을 정한거야~!!! # 세션 변수에 인덱스를 넣는다(회원주소)
                    print(f"{m[1]}님 로그인이 되었습니다.")
                    print(f"{m[3]}권한으로 로그인이 되었습니다.")

                # 관리자 메뉴 3번을 더 작성해서 해봐!

                    return # member_login()종료
                else: # if m[1] == pw: 결과가 false 이면
                    print("비밀번호가 맞지 않습니다. 초기메뉴로 돌아갑니다.")
                    return # member_login()종료
        else:  #for문에 리턴이 안걸리면 여기까지와서 프린트 된다
            print("존재하지 않는 아이디입니다.")
            return

    def member_logout(self):                                           # 로그아웃하기
        if self.session is None:
            print(" 로그인 후 이용 가능합니다.")
            return
        self.session = None  # 세션값에 있는 인덱스를 None 처리
        print(" 로그아웃 처리 되었습니다.")

    def member_list(self):                                             #회원 목록 전제보기
        if self.session is None:
            print(" 로그인 후 이용 가능합니다.")
            return

        print("\n 회원 목록")
        print("-" * 60)
        print(f"{'ID':10} {'이름':10} {'권한':10} {'상태':10}")
        print("-" * 60)
        for idx, m in enumerate(self.members):
            if m[4] == True:
                m[4] = "활성화"
            else:
                m[4] = "비활성화"
            print(f"{m[0]:10} {m[1]:10} {m[3]:10} {m[4]:10}")
            print("-" * 60)

    def member_modify(self):   # 머디파이는 수정하는거                     # 회원 정보 수정 하기!!
        if self.session is None:
            print(" 로그인 후 이용 가능합니다.")
            return
        else:
            print(f"아이디는 : {self.members[self.session][0]}, 이름은 : {self.members[self.session][1]}")
            print(f"비밀번호는 : {self.members[self.session][2]} 입니다.")
            print("===회원 정보 수정===")
            print("1, 아이디변경  2. 이름 변경 3. 비밀번호 변경 ")
        sel = input("선택 :")
        if sel == "1":
            self.members[self.session][0] = input("변경할 아이디 : ")
            # 2차원 배열에[로그인 인덱스 idx] [m 아이디위치]
            print(f"아이디가 {self.members[self.session][0]}으로 변경되었습니다.")
        elif sel == "2":
            self.members[self.session][1] = input("변경할 이름: ")
            print(f"이름이 {self.members[self.session][1]}으로 변경되었습니다.")
        elif sel == "3":
            self.members[self.session][2] = input("변경할 비밀번호 : ")
            print(f"비밀번호가 {self.members[self.session][2]}으로 변경되었습니다.")

            self.save_members()  # 여기에 저장
            self.load_member()  # 저장했다 다시불러오기
        else:
            print("잘못입력하셨습니다.")
            return

    def member_delete(self):                                            # 회원 탈퇴 하기
        if self.session is None:
            print(" 로그인 후 이용 가능합니다.")
            return

        print("\n [ 회 원 탈 퇴 ] ")
        print(" 1. 완전 탈퇴 ")
        print(" 2. 계정 비활성화 ")
        sel = input("선택 번호 : ")
        if sel == "1":
            print(f"{self.members[self.session][0]}님의 계정을 탈퇴합니다.")
            self.members.pop(self.session)
        elif sel == "2":
            print(f"{self.members[self.session][0]}님의 계정을 비활성화합니다.")
            self.members[self.session][4] = False
        self.session = None
        self.save_members()
        self.load_member() # 수정후 다시불러오는겨 갱신을 여디서 할찌 run 시작에서 할지 결정해바
        print("처리 완료 되었습니다.")

    def member_admin(self):  # 로그인시 admin = role이면 진입하게 만들어!!            # 관리자 메뉴 !!
        print("\n [ 관 리 자 메 뉴 ] ")
        print(" 1. 비밀번호 변경")
        print(" 2. 블랙 리스트 설정")
        print(" 3. 권한 변경")
        print(" 0. 종료")

        sel = input("선택 : ")  # 관리자 메뉴 선택용
        uid = input("대상 아이디 : ") # 대상아이디 찾는 입력
        for m in self.members: # 멤버스의 2차원 배열을 반복하고 있어~
            if m[0] == uid:    # 대상아이디를 찾으면
                if sel == "1": # 비밀번호 변경
                    m[2] = input("변경될 비밀번호: ")
                    print(f"{m[0]}님 비밀번호가 {m[2]}로 변경되었습니다.")
                    return
                elif sel == "2": # 블랙리스트처리
                    print(f"현재상태는 {m[4]}입니다")
                    setsel = input("변경하시려면 y: ")
                    if setsel == "y":
                        m[4] = False
                        print(f"{m[0]}님의 계정이 비활성화 되었습니다.")
                        return

                elif sel == "3": # 권한변경
                    print(f"현재상태는 {m[3]}입니다")
                    print("\n [ 권 한 변 경 ] ")
                    print(" 1, admin")
                    print(" 2, manager")
                    print(" 3, user")
                    subsel = input("선택번호 입력 : ")
                    if subsel == "1":
                        m[3] = "admin"
                        print(f"{m[0]}님 {m[3]}으로 권한이 변경되었습니다.")
                    elif subsel == "2":
                        m[3] = "manager"
                        print(f"{m[0]}님 {m[3]}으로 권한이 변경되었습니다.")
                    elif subsel == "3":
                        print()
                        m[3] = "user"
                        print(f"{m[0]}님 {m[3]}으로 권한이 변경되었습니다.")

                    self.save_members() # 파일로 저장
                    self.load_member()
                    print("관리자 작업 완료")
                    return
                else:
                    print(" 잘못입력하셨습니다. ")

#-----------------------------메뉴 만들기----------------------------
    def main_menu(self):
        print(f"""
        ==== 엠비씨아카데미 회원관리 프로그램입니다======
        1. 회원가입       2. 로그인      3. 로그아웃
        4. 회원 정보 보기  5. 회원정보수정   
        6. 회원탈퇴       7. 관리자메뉴

        9. 프로그램 종료
        """)

    # ===============================
    # 실행
    # ===============================
    def run(self):
        while True:
            self.main_menu()
            sel = input(">>> ")

            if sel == "1": self.member_add()
            elif sel == "2": self.member_login()
            elif sel == "3": self.member_logout()
            elif sel == "4": self.member_list()
            elif sel == "5": self.member_modify()
            elif sel == "6": self.member_delete()
            elif sel == "7": self.member_admin()
            elif sel == "9": break


# ===============================
# 프로그램 시작
# ===============================
app = MemberManager()   # 가장 중요한 포인트 (지금까지 만든 클래스를 객체로 만들고)
app.run()               # 객체에 있는 .run()매서드를 실행한다
