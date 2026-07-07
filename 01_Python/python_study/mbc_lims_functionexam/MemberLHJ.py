run = True # while에서 전제척으로 사용되는 변수(프로그램 구동)
session = None #로그인상태 저장용 -> 로그인한 사용자의 리스트 인덱스 기억용
# from tabulate import tabulate
#프로그램에서 사용될 리스트들 (더미 데이터)
# sns = [1,2,3]   # 회원번호 회원 삭제및 추가시 번호가 흔들릴수있음(인덱스로만 써보자)
ids = ["kkw","lhj","ljj"]   # 로그인 아이디 들
pws = ["1234","0000","8888"]   # 암호 들
names = ["김기원","임효정","이재정"] # 사용자 명
roles = ["admin","manager","user"] # 사용자 권한(admin, manager, user)
active = [True,True,True] #회원 사용중, 탈되, 중지, 블랙리스트등... True, False
# 차후에는 파일처리로 변환 할 예정

#프로그램에서 사용될 함수들

def member_add():
    print("member_add 함수로 진입합니다.")
    print("회원 가입을 시작합니다.")
    new_id = input("아이디 : ")
    if new_id in ids:
        print("이미 존재하는 아이디입니다.")
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
아이디 : {new_id}  암호 : {new_pw}
이름 : {new_name}   권한 : {new_role}""")

        save_select = input("저장하려면 y : ")
        if save_select == "y":
            ids.append(new_id)
            pws.append(new_pw)
            names.append(new_name)
            roles.append(new_role)
            active.append(True)
            print("저장되었습니다.")
        else:
            print("회원가입이 되지 않았습니다.")
   # print("member_add 함수를 종료합니다.")

def member_login():
    print("member_login 함수로 진입합니다.")

    global session  #맨위에 있는 함수를 사용하겠다!!!

    if session is not None: #논값이 아닐경우 로그인중이다!
        print("이미 로그인한 상태입니다.")
        print(f"로그인한 사용자는 {names[session]}.")
        return
    else:
        user_id = input("로그인 ID : ")
        user_pw = input("비밀번호 : ")

        if user_id in ids: #로그인한 아이디가 리스트에 있으면
            idx = ids.index(user_id)  # 해당주소를 idx에 넣어라~
            if not active [idx] :  # 그리고 회원이 활성화,비활성화인지를 또 물어!!!
                # not는 False값  True문에서 not처리했잖아~!!
                print("비활성화/차단된 계정입니다.")
                return

            else:
                if user_pw == pws[idx] : #이게 참일경우야~
                    session = idx  #세션이 로그인한상태야~~
                    print(f"{names[session]}님 환영합니다.")
                    print(f"{roles[idx]}권한을 가지고 있습니다.")
                else:
                    print("비밀번호가 다릅니다.")
        else:
            print("존재하지 않는 아이디입니다.")
    print("member_login함수를 종료합니다.")

def member_admin():
    global session
    if session is None:
        print("로그인 후 이용가능합니다.")

    elif roles[session] == "admin":

        print("member_admin 함수로 진입합니다.")
        print("\n [관리자 메뉴입니다.]")
        print("1. 회원비밀번호 변경")
        print("2. 회원 블랙리스트 처리")
        print("3. 권한 변경")
        print("0. 종료")

        sel = input(">>>")
        if sel == "1":
            adm = input("대상 아이디 : ")
            if adm in ids:
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