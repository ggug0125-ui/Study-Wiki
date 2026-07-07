import os



run = True  # while 에서 전체적으로 사용되는 변수(프로그램 구동)

session = None  # 로그인상태 저장용 -> 로그인한 사용자의 리스트 인덱스 기억용
FILE_NAME = "members.txt"  # 회원정보를 저장할 메모장 파일명
members = []  # 지금은 비어있지만 좀있다 메모장에 있는 내용을 가져와 리스트 처리를 할꺼임

def save_members():
    """
    members 2차원 리스트 내용을 members.txt파일에 저장
    """
    with open(FILE_NAME, "w", encoding="utf-8") as f:  # f는 열린 파일

        for member in members:  # members 메모리에 있는 2차원 배열 을 member에 하니씩 넣는다.
            line = f"{member[0]}|{member[1]}|{member[2]}|{member[3]}|{member[4]}\n"

            f.write(line)  # 열린 파일 메모장에 저장하는거다!!




def load_members():  # 텍스트 파일을 전체 불러와 리스트로 만듬~!!왜??? 중간수정이 안대~
    """
    member.txt 파일을 읽어서 members리스트에 저장
    """
    # 파일이 없으면 새파일 생성(암기해~!!)
    if not os.path.exists(FILE_NAME):  # 지금 디렉토리에 FILE_NAME이 없으면!!!
        save_members()  # 빈파일이 member.txt 로 생성됨 세이브멤버스 함수에 새파일만드는게 있어
        return

    with open(FILE_NAME, "r", encoding="utf-8") as f:

        for line in f:  # f 파일내용을 한줄씩 line 변수에 넣음

            data = line.strip().split("|")  # | =>  리스트화만들기(   ,   ,   ,  )

            data[4] = True if data[4] == "True" else False  # "True" 따옴표 없애라

            print(f"변조후 데이터 : {data}")
            # print("----------------------------")


            members.append(data)


# load_member()함수종료

# 프로그램에서 사용될 함수들
def member_add():
    # 회원가입용 함수
    print("member_add 함수로 진입합니다.")
    # 회원가입에 필요한 기능을 넣음
    uid = input("아이디: ")
    # 아이디 중복검사
    for member in members:
        if member[0] == uid:  # {member[0]}|{member[1]}|{member[2]}|{member[3]}|{member[4]}
            #                       id         pw         name        role        active
            print("이미 존재하는 아이디입니다.")
            return  # 돌아가~ 함수를 빠져나와 메인메뉴로 돌아감!!
        # else 처리 없이 return으로 처리함

    pw = input("비밀번호: ")
    name = input("이름: ")

    # 권한 선택
    print("1. admin     2. manager     3. user  ")
    roleSelest = input("권한 선택 : ")

    role = "user"  # 잘못 클릭해도 user권한으로 기본값
    if roleSelest == "1":
        role = "admin"
    elif roleSelest == "2":
        role = "manager"
        # ================ 입력값 완성  ===============
    print(f"아이디 : {uid}  이름 : {name} ")
    print(f"권한 : {role} 암호 : {pw} ")
    # =======입력값확인

    save_True = input("저장하려면 y를 누르세요 : ")
    if save_True == "y":
        # 저장시작
        members.append([uid, name, pw, role, True])  # 리스트로 만듬 이차원배열로 박는다
        save_members()  # 리스트를 파일에 저장
        print("회원가입을 완료합니다.")
    # member_add() 함수 종료
    print("member_add 함수를 종료합니다.")


# 회원가입용 함수 종료


def member_login():
    # 가입된 회원을 확인하여 로그인 처리 후 session 변수에 인덱스를 넣음
    print("member_login 함수로 진입합니다.")
    # 로그인에 필요한 기능을 넣음
    # 이미 파일을 불러온 상태야~~
    global session  # 전역변수로 생성한 값을 가져옴!!(이미 로그인한상태일수도있고 or Nome)
    #                                                   인덱스
    uid = input("아이디 : ")
    pw = input("비밀번호 : ")  # 키보드와 비밀번호를 입력하고 변수에 넣어라~
    # 이 다음에 회원 목록에서 아이디를 찾아~~
    for idx, member in enumerate(members):  # 이번엔 다르게 만들어보쟈~~
        #    0   [kkw,김기원....]  enumerate는 멤버스에서 idx와 멤버로 빼준다~!!
        # enumerate() for문은 반목문으로 인덱스를 찾아옴
        # idx => 1차원 주소
        # member => 2차원 주소
        # print("idx : ", idx) # -> 1차원 주소
        # print("member : ", member) # -> 2차원 주소
        # print("member[0] : ", member[0])
        # print("member[1] : ", member[1])
        # idx: 0
        # member: ['kkw', '김기원', '0000', 'admin', True]
        # member[0]: kkw
        # member[1]: 김기원

        if member[0] == uid:  # 키보드로 입력한 uid와 리스트에 있는값이 같으면 아이디찾아
            if not member[4]:  # 엑티브 활성화상테가 False
                print("로그인할수없는 계정입니다.. (블랙리스트, 비활성화)")
                return  # 로그인중단 member_login()함수를 종료
            if member[2] == pw:  # 키보드로 입력한 암호와 리스트[2]암호가같으면
                session = idx  # 전역변수에 로그인한 주소를 넣음
                print(f"{member[1]}님 로그인이 되었습니다.")
                print(f"{member[3]}권한으로 로그인이 되었습니다.")
                return

            else:
                print("비밀번호가 맞지 않습니다. 초기메뉴로 돌아갑니다.")
                return  # member_login()함수를 종료

    else:  # for문안에서 구동하면 반복 구동해서 다출력된다!!!
        print(" 찾는 아이디가 없습니다.")  # for로 찾으면서 없으면 출력이될수있다!!!


    print("member_login 함수를 종료합니다.")


# 회원로그인용 함수 종료


def member_admin():
    # 관리자가 로그인 했을 경우 할수 있는 기능을 작성
    print("member_admin 함수로 진입합니다.")
    print("\n [ 관리자 메뉴 ]")
    print("1. 비밀번호 변경")
    print("2. 블랙리스트 처리 ")
    print("3. 권한 변경")
    print("0. 종료")

    sel = input("선택 : ")
    uid = input("대상아이디 : ")
    # 다른 사용자 암호 변경 코드
    for member in members:
        if member[0] == uid:
            if sel == "1":
                member[2] = input("변경될 비밀번호 : ")
                print(f"{member[0]}님 비밀번호가 {member[2]}로 변경되었습니다")
                return
            elif sel == "2":
                member[4] = False
                print(f"{member[0]}님의 계정이 비활성화되었습니다.")
            elif sel == "3":
                print("\n [ 권 한 변 경 ] ")
                print(" 1, admin")
                print(" 2, manager")
                print(" 3, user")
                subsel = input("선택번호 입력 : ")
                if subsel == "1":
                    member[3] = "admin"
                    print(f"{member[0]}님 {member[3]}으로 권한변경되었습니다.")
                elif subsel == "2":
                    member[3] = "manager"
                    print(f"{member[0]}님 {member[3]}으로 권한변경되었습니다.")
                elif subsel == "3":
                    member[3] = "user"
                    print(f"{member[0]}님 {member[3]}으로 권한변경되었습니다.")
                else:
                    print("잘못눌렀습니다.")

    # 블랙리스트로 변환 -> active를 False

    # 권한 부여 -> 사용자의 권한roles를 변경 (manage <-> user)

    print("member_admin 함수로 종료합니다.")


# 관리자가 사용자 변경사항 함수 종료

def member_logout():
    # 회원 로그아웃으로 상태 변경 -> session 값을 None으로 변경
    print("member_logout 함수로 진입합니다.")
    # 로그인 상태인지를 확인하고 session을 None으로 변경
    global session
    for idx, member in enumerate(members):
        if session is None:
            print("로그인후 이용가능 합니다.")
            return
        else:
            lout = input("비밀번호 : ")
            if lout == member[2]:
                print(f"{member[1]}님 로그아웃 되었습니다.")
                session = None
                break
            else:
                print("비밀번호가 틀립니다.")
                break

    print("member_logout 함수를 종료합니다.")


# 로그아웃 함수를 종료

def member_modify():
    # 회원 정보 수정
    print("member_modify 함수로 진입합니다.")
    # 로그인 상태인지를 확인하고 자산의 정보를 확인하고 수정한다.
    global session
    for idx, member in enumerate(members):
        if session is None:
            print("로그인후 이용가능 합니다.")
            return
        else:
            print(f"아이디는 : {members[session][0]}, 이름은 : {members[session][1]}")
            print(f"비밀번호는 : {members[session][2]} 입니다.")
            print("===회원 정보 수정===")
            print("1, 아이디변경  2. 이름 변경 3. 비밀번호 변경 ")
            sel = input("선택 :")
            if sel == "1":
                members[session][0] = input("변경할 아이디 : ")
                print(f"아이디가 {members[session][0]}으로 변경되었습니다.")
                break
            elif sel == "2":
                members[session][1] = input("변경할 이름: ")
                print(f"이름이 {members[session][1]}으로 변경되었습니다.")
                break
            elif sel == "3":
                members[session][2] = input("변경할 비밀번호 : ")
                print(f"비밀번호가 {members[session][2]}으로 변경되었습니다.")
                break
            else:
                print("잘못입력하셨습니다.")
                return
    save_members()
    print(" 처리 되었습니다.")

    print("member_modify 함수를 종료합니다.")


# 회원정보 수정 종료

def member_delete():
    # 회원 탈퇴 또는 회원 유휴등 처리
    print("member_delete 함수로 진입합니다.")
    # 로그인 상태인지를 확인하고 탈퇴는 pop, 유휴(active=False)
    global session
    if session is None:
        print("로그인 후 이용 가능합니다.")
        return
    print("\n [ 회 원 탈 퇴 ]")
    print("1. 완전 탈퇴")
    print("2. 계정 비활성화")

    sel = input(" 선택번호 : ")

    if sel == "1":
        print(f"{members[session][0]}님의 계정을 탈퇴합니다.")
        members.pop(session)
        session = None

    elif sel == "2":
        print(f"{members[session][0]}님의 계정을 비활성화 합니다.")
        members[session][4] = False
        session = None

    save_members()
    print(" 처리 되었습니다.")
    print("member_delete 함수를 종료합니다.")


def show_members_list():
    global session
    if session is None:
        print("로그인 후 이용 가능합니다.")
        return

    print("\n 회원 목록")
    print("-" * 60)
    print(f"{'ID':10} {'이름':10} {'권한':10} {'상태':10}")
    print("-" * 60)
    for idx, member in enumerate(members):
        if member[4] == True:
            member[4] = "활성화"

        else:
            member[4] = "비활성화"

        print(f"{member[0]:10} {member[1]:10} {member[3]:10} {member[4]:10}")
        print("-" * 60)


# 회원탈퇴 종료

# --------------------- 기능에 대한 함수 생성 끝----------------

def main_menu():
    print(f"""
    ==== 엠비씨아카데미 회원관리 프로그램입니다======
    1. 회원가입       2. 로그인      3. 로그아웃
    4. 회원 정보 보기  5. 회원정보수정   
    6. 회원탈퇴       7. 관리자메뉴

    9. 프로그램 종료
    """)


# 메인메뉴용 함수 종료

def login_menu():
    print(f"""
    -----------로그인 전용 메뉴 입니다------------
    1. 회원 정보 보기
    2. 회원 정보 수정
    3. 회원 탈퇴
    4. 회원 정보 보기
    5. 관리자 메뉴
    6. 로그아웃 
    0. 나가기
    """)


# ------------------ 메뉴 함수 끝 ------------------
load_members()  # 프로그램 시작시 파일을 불러오기 ->이차원 배열로 한번만 불러오기한거다
print(members)

# 프로그램 시작!!!!
while run:  # 주실행코드
    main_menu()  # 위에서 만든 메인메뉴를 실행
    select = input(">>>")  # 키보드로 메뉴선택
    if select == "1":  # 회원가입 코드
        member_add()  # 회원가입용 함수 호출



    elif select == "2":  # 로그인 메뉴 선택
        member_login()  # 로그인용 함수 호출

    elif select == "3":  # 로그아웃 메뉴 선택
        member_logout()  # 로그아웃 함수 호출

    elif select == "4":
        show_members_list()

    elif select == "5":  # 회원정보 수정 선택
        member_modify()  # 회원정보 수정 함수 호출

    elif select == "6":  # 회원 탈퇴 선택
        member_delete()  # 회원 탈퇴 함수 호출

    elif select == "7":
        member_admin()

    elif select == "9":  # 프로그램 종료
        run = False
    else:
        print("잘못 입력하셨습니다.")
