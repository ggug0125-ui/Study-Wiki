import os # 그냥 넣어놔 밑에 쓰여야해!!!!


run = True  # while 에서 전체적으로 사용되는 변수(프로그램 구동)
session = None  # 로그인상태 저장용 -> 로그인한 사용자의 리스트 인덱스 기억용
FILE_NAME = "members.txt"  #회원정보를 저장할 메모장 파일명
members = []  #지금은 비어있지만 좀있다 메모장에 있는 내용을 가져와 리스트 처리를 할꺼임
# members 구조:
# [아이디, 비밀번호, 이름, 권한, 활성화 여부]
# "kkw" "1234" " 김기원" "admin" "True"
# kkw|1234|김기원|admin|True 로 메모장에 저장될 예정임

#파일 처리용 함수들!!

def save_members():
    # 파일 저장함수~~~~~~
    """ ->이건 개발자끼리 보인다~ 주석처리 안해도 구동에는 문제없다~!!!
    members 리스트 내용을 members.txt파일에 저장

    """
    with open(FILE_NAME, "w", encoding="utf-8") as f:  # 파일을 열자! 인코딩 "UTF-8" 방식으로열어! 열어서 f(객체)에 넣어
    # with는 열구 닫는걸 다 포함한 함수~
        for member in members: # 이렇게 저장해라~
            line = f"{member[0]},{member[1]},{member[2]},{member[3]},{member[4]}\n"
            f.write(line) # 메모장에 저장했다 (회원리스트보기와 같어~ 프린트하느냐 그걸 저장하느냐 차이야!!)


def load_members():
    # 파일 읽기 함수~~~~~
    if not os.path.exists(FILE_NAME): # 찾는 파일이 없어??
        save_members()  # 빈 파일 하나 만들어~
        return # 다시 돌아가~
    with open(FILE_NAME, "r", encoding="utf-8") as f: # 멤버스파일있으면 읽기전용으로 열구문닫아 f 변수객체~!!

        for line in f: #f 변수에 한줄씩 넣는거야~
            print(f"변조전 데이터 : {line}")  # 다닥다닥 붙어있어 "|"
            data = line.strip().split("|")  # 라인맨뒤에 엔터지우고, "|"이거 지워~!
            print(f"변조후 데이터 : {data}")  # 출력해바
            print("===================")
            data[4] = True if data[4] == "True" else False  # 패션코드야 쓰지말어
            # 내가 배운걸로 써보면
            #if data[4] == "True" :
            #   data[4] = True
            #else :
            #  data[4] = False
            # 받은변수값이 데이터 4번째 문자열이 맞으면 아니면???
            print(f"변조후 데이터 : {data}")
            print("===================")
            members.append(data)


def member_add():
    load_members()
    print("member_add 함수로 진입합니다.")
    print("회원 가입을 시작합니다.")

    uid = input("아이디 : ")
    is_exists = False
    if uid in members == data[0]: # 파일 아이디는 어떻게 빼오는거야!!? 인덱스번호 쳐??
        print("존재하는 아이디가 있습니다.")
        return

    else:
        new_pw = input("비밀번호 : ")
        new_name = input("이름 : ")
        member_add_menu()
        role_set = input("권한을 선택하세요 : ")
        if role_set == "1":
            new_role = "admin"
        elif role_set == "2":
            new_role = "manager"
        else:
            new_role = "user"
        print(f"""
입력된 정보를 확인하세요 
아이디 : {uid}  암호 : {new_pw}
이름 : {new_name}   권한 : {new_role}""")

        save_select = input("저장하려면 y : ")
        if save_select == "y":
            save_members()
            print("저장되었습니다.")
        else:
            print("회원가입이 되지 않았습니다.")
   # print("member_add 함수를 종료합니다.")

def member_login():
    print("member_login 함수로 진입합니다.")
    global session
    load_members()


    if session is not None: #논값이 아닐경우 로그인중이다!
        print("이미 로그인한 상태입니다.")
        print(f"로그인한 사용자는 {data[0]}.") # 이름을 어떤식으로 빼오냐???
        return
    else:
        user_id = input("로그인 ID : ")
        user_pw = input("비밀번호 : ")

        if user_id in load_members(): #로그인한 아이디가 리스트에 있으면
            idx = os.id.index(user_id)  # 해당주소를 idx에 넣어라~
            if not os.id.index(user_id) :  # 그리고 회원이 활성화,비활성화인지를 또 물어!!!
                # not는 False값  True문에서 not처리했잖아~!!
                print("비활성화/차단된 계정입니다.")
                return

            else:
                if user_pw == load_members() : #이게 참일경우야~
                    session = idx  #세션이 로그인한상태야~~
                    print(f"{os.name[session]}님 환영합니다.")
                    print(f"{os.role}권한을 가지고 있습니다.")
                else:
                    print("비밀번호가 다릅니다.")
        else:
            print("존재하지 않는 아이디입니다.")
    print("member_login함수를 종료합니다.")

def member_admin():
    global session
    if session is None:
        print("로그인 후 이용가능합니다.")

    elif os.role[session] == "admin":

        print("member_admin 함수로 진입합니다.")
        print("\n [관리자 메뉴입니다.]")
        print("1. 회원비밀번호 변경")
        print("2. 회원 블랙리스트 처리")
        print("3. 권한 변경")
        print("0. 종료")

        sel = input(">>>")
        if sel == "1":
            adm = input("대상 아이디 : ")
            if adm in ids:  # 파일에서 어떻게 찾아야하는지 몰라!!!!
                idx = ids.index(adm)
                print("기존 비밀번호 : " + pws[idx])
                pws[idx] = input("변경할 비밀번호 : ")
                print("비밀번호가 변경되었습니다.")
            else:
                print("아이디를 잘못입력했습니다.")
                member_admin()
        if sel == "2":
            adm = input("대상아이디 : ")
            if adm in ids:
                idx = ids.index(adm)
                active[idx] = False
                print(f" id: {ids[idx]}, 이름: {names[idx]}, 권한: {roles[idx]}님 ")
                print("블랙리스트 처리가 되었습니다.")

            else:
                print("아이디를 잘못입력했습니다.")
                member_admin()
        if sel == "3":
            adm = input("대상 아이디: ")
            if adm in ids:
                idx = ids.index(adm)
                print(" 변경할 권한을 입력하세요 (admin / manager / user)")
                roles[idx] = input("새 권한입력 : ")
                print(f"id: {ids[idx]}, 이름: {names[idx]}님")
                print(f"권한: {roles[idx]}으로 변경되었습니다.")
            else:
                print("아이디를 잘못입력했습니다.")
                member_admin()

    else:
        print("관리자 계정이 아닙니다.")
    print("member_admin를 종료합니다.")

def member_logout():
    global session
    if session is None:
        print("로그인 후 이용가능합니다.")
    else:
        lout = input("비밀번호 : ")
        if lout == pws[session]:
            print(f"{ids[session]}님 로그아웃이 되었습니다.")
            session = None
        else:
            print("비밀번호가 틀립니다.")

    print("member_logout를 종료합니다.")

def member_modify():
    if session is None:
        print("로그인 후 이용가능합니다.")
        return

    print("내정보는")
    print(f"{ids[session]},{pws[session]},{names[session]}")
    print(f"{roles[session]} 입니다.")
    print("""
    -----변경할 정보 선택 -----
    1. 이름변경  2. 비밀번호 변경 3. 관리자권한변경
    ((권한변경은 관리자메뉴로 돌아갑니다.)) """)

    sel = input("선택 : ")
    if sel == "1":
        names[session] = input("변경할 이름 : ")
        print(f"{names[session]}으로 변경되었습니다.")
    elif sel == "2":
        pws[session] = input("변경할 비밀번호 :")
        print(f"{pws[session]}으로 변경되었습니다.")
    elif sel == "3":
        print("관리자 메뉴로 진입합니다.")
        member_admin()

    print("member_modify를 종료합니다.")


def member_delete():
    global session
    if session is None:
        print("로그인후 이용가능합니다.")
        return
    print (""" 
    == 엠비씨 아케데미 회원 관리프로그램 ==
    1. 회원탈퇴 2. 계정비활성화 """)

    sel = input("선택번호 입력 : ")
    if sel == "1":
        print(f"{ids[session]},{pws[session]},{names[session]}")
        print(f"{roles[session]} 님")
        dea = input(" 회원 탈퇴를 하시겠습니까? y/n : ")
        if dea == "y":
            print("회원탈퇴가 완료되었습니다.")
            ids.pop(session)
            pws.pop(session)
            names.pop(session)
            roles.pop(session)
            active.pop(session)
            session = None
        else:
            print("회원탈퇴가 취소 되었습니다.")
    elif sel == "2":
        print(f"{ids[session]},{pws[session]},{names[session]}")
        print(f"{roles[session]} 님")
        print("계정 비활성화를 완료합니다.")
        active[session] = False
        session = None


    print("member_delete를 종료합니다.")

def mamber_list():
    global session
    if session is None:
        print("로그인후 이용가능합니다.")

    elif roles[session] == "manager" or roles[session] == "admin":
        print("회원 정보 리스트 입니다.")
        print("---------------------------------")
        print("       [ 회  원  목  록 ]  ")

        for i in range(len(ids)):
            print(f"ID:{ids[i]}, 이름:{names[i]}, 권한:{roles[i]},상태:{active[i]}")
    else:
        print(" 회원 보기 권한이 없습니다.")

def main_menu():
    print(f"""
    ====== 엠비씨아카데미 회원 관리 프로그램입니다 ======
    1. 회 원 가 입     2. 로 그 인    3. 로그아웃  
    4, 회원 정보 보기   5. 회원정보수정 
    6. 회 원 탈 퇴     7. 관리자메뉴
    9. 프로그램 종료

    """)


# 메인메뉴용 함수 종료
def member_add_menu():  # 회원 가입에서 사용할 메뉴
    print(f"""
    -- 회원 권한을 확인합니다 --
    1. 관리자  2. 팀장  3. 일반사용자
          """)
#====================================================================
while run: #주실행코드
    main_menu() # 위에서 만든 메인메뉴를 실행
    select = input(">>>") #키보드로 메뉴선택
    if select == "1": # 회원가입 코드
        member_add()  # 회원가입용 함수 호출

    elif select == "2": # 로그인 메뉴 선택
        member_login()  # 로그인용 함수 호출

    elif select == "3":  # 로그아웃 메뉴 선택
        member_logout()  # 로그아웃 함수 호출

    elif select == "4":
        mamber_list()

    elif select == "5":  # 회원정보 수정 선택
        member_modify()  # 회원정보 수정 함수 호출

    elif select == "6": # 회원 탈퇴 선택
        member_delete() # 회원 탈퇴 함수 호출

    elif select == "7":
        member_admin()

    elif select == "9": # 프로그램 종료
        run = False
    else:
        print("잘못 입력하셨습니다.")