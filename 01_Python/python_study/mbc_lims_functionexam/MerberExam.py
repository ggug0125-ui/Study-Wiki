# 회원관리 C R U D를 사용자 지정 함수로 만들어보자
# C : 회원가입
# R : 회원 리스트 전제 보기 후 관리자인 경우 회원암호 변경, 블랙리스트 생성, 권한 부여
# R : 로그인 id와 pw를 활용하여 로그인 상태 유지 session
# U : 회원 정보 수정
# D : 회원 탈퇴, 회원비활성화

# 프로그램에서 사용될 변수들
# 전역변수 (global) -> 파일안에서 전체적으로 사용되는변수
# 지역변수 (local) -> while, if, for, def 안에서 사용되는 변수
run = True # while에서 전제척으로 사용되는 변수(프로그램 구동)
session = None #로그인상태 저장용 -> 로그인한 사용자의 리스트 인덱스 기억용

#프로그램에서 사용될 리스트들 (더미 데이터)
# sns = [1,2,3]   # 회원번호 회원 삭제및 추가시 번호가 흔들릴수있음(인덱스로만 써보자)
ids = ["kkw","lhj","ljj"]   # 로그인 아이디 들
pws = ["1234","5678","8888"]   # 암호 들
names = ["김기원","임효정","이재정"] # 사용자 명
roles = ["admin","manager","user"] # 사용자 권한(admin, manager, user)
active = [True,True,True] #회원 사용중, 탈되, 중지, 블랙리스트등... True, False
# 차후에는 파일처리로 변환 할 예정

#프로그램에서 사용될 함수들

def member_add():
    #회원가입용 함수
    print("member_add 함수로 진입합니다.")
    # 회원 가입에 필요한 기능을 넣음
    new_id = input("아이디 :") # new_id는 로컬함수야~~~
    # 이미 아이디가 존재하면 다른아이디로 넣게 유도
    if new_id in ids: #아이디리스트에서 찾아 있는지 확인해~
        #Trus일때
        print("이미 존재하는 아이디입니다.")
        return # if문 종료 -> 상위메뉴로 이동
    else: #False 아이디리스트에 입력된 아이디가 없을때 (중복없다)
        new_pw = input("비밀번호 : ")
        new_name = input("이름 : ")
        member_add_menu() # 회원 권한 메뉴 출력
        role_set = input("권한 선택 : ")  # role_set 로컬함수야~~~
        if role_set == "1":
            new_role = "admin"
        elif role_set == "2":
            new_role = "manager"
        else:
            new_role = "user"
        print(f""" 
        입력된 정보를 확인하세요
        이름 : {new_name} 암호 : {new_pw}
        아이디 : {new_id} 권한 : {new_role}""")
        #print("저장하려면 Y : ")

        save_select = input("저장하려면 Y : ")
        if save_select == "y":
            print("저장을 시작합니다")
            ids.append(new_id)
            pws.append(new_pw)
            names.append(new_name)
            roles.append(new_role)
            active.append(True)
            print("저장완료")
            #차후에 로그인 함수를 추가해봄
        else:
            print("회원가입이 되지 않았습니다.")
    print("member_add 함수를 종료합니다.")
    # 회원가입용 함수 종료

def member_login():
    # 가입된 회원을 확인하여 로그인 처리후 session 변수에 인덱스를 넣음
    print("member_login 함수로 진입합니다.")
    # 로그인에 필요한 기능을 넣음

    global session #맨위에 전역변수로 지정한 내용을 활용하겠다.

    if session is not None: #로그아웃상태가 아닌상태 session에 이미 값이있으면??
    # is not None 싱글톤이라는 객체가 있는지 비교하는 용
    # if session != None - > 숫자 비교형 이퀄이나는 값으로 사용
        #True
        print("이미 로그인한 상태입니다.")
        print(f"로그인한 사용자는 {names[session]}님 입니다.") #session이 2번이면 이재정

        return  #되돌아가기
    else:
        #False 로그인을 안한상태
        user_id = input("로그인 ID : ")
        user_pw = input("비밀번호 : ")

        if user_id in ids : #키보드로 받은 아이디를 아이디리스트에 있는지?
            # True 있으면
            idx = ids.index(user_id)  #아이디에 해당하는주소를 idx로 넣음
            if not active [idx] : #회원활성화 상태인지확인, 탈퇴한 아이디 거르기
                #False 면
                print("비활성화/차단된 계정입니다.")
                return

            else:
                #True
                #암호를 비교
                if user_pw == pws[idx] : #키보드로 넣은 암호와 리스트의 주소암호 일치
                    # id도 같고 활성화상태거 암호가 같다
                    session = idx #로그인상태
                    # 글로벌영역에 session값(로그인한 사용자의 주소)이 있는상태
                    print(f"{names[session]}님 환영합니다.") #idx넣어도 상관없음
                    print(f"{roles[idx]}권한을 가지고 있습니다.") #둘다 써봐

                else: #패스워드가 잘못된값일경우
                    print("비밀번호가 다릅니다.")


        else:
            print("존재하지 않는 아이디입니다.")



    print("member_login 함수를 종료합니다.")
    # 회원 로그인용 함수 종료

def member_admin():
    # 관리자가 로그인했을경우 할수있는 기능을 작성
    print("member_admin 함수로 진입합니다.")
    # 다른 사용자 암호 변경코드

    # 블랙리스트로 변환 - > active를 False

    # 권한 부여 -> 사용자의 권한 roles를 변경 (manager <-> user)


    print("member_admin 함수를 종료합니다.")
    #관리자가 사용자 변경사항 함수 종료

def member_logout():
    # 회원 로그아웃으로 상태 변경 -> session 값을 None으로 변경
    print("member_logout 함수로 진입합니다.")
    # 로그인 상태인지를 확인하고 session을 None으로 변경


    print("member_logout 함수룰 종료합니다.")
    # 로그아웃 함수를 종료

def member_modify():
    # 회원 정보 수정
    print("member_modify 함수로 진입합니다.")
    # 로그인 상태인지를 확인하고 자신의 정보를 확인하고 수정한다

    print("member_modify 함수를 종료합니다.")
    # 회원정보 수정 종료

def member_delete():
    #회원 탈퇴 또는 회원 비활성화(유휴) 등 처리
    print("member_delete 함수로 진입합니다.")
    # 로그인 상태인지를 확인하고 탈퇴는 pop, 유휴는(active = False)

    print("member_delete 함수를 종료합니다.")
    # 회원 탈퇴 종료

#---------------------------------------여기까지가  기능에 대한 함수 생성 끝----------

def main_menu():
    print(f"""
    ====== 엠비씨아카데미 회원 관리 프로그램입니다 ======
    1. 회원가입    2. 로그인   3. 로그아웃  
    4. 회원정보수정 5. 회원탈퇴
    9. 프로그램 종료
    
    """)
# 메인메뉴용 함수 종료
def member_add_menu():  # 회원 가입에서 사용할 메뉴
    print(f"""
    -- 회원 권한을 확인합니다 --
    1. 관리자  2. 팀장  3. 일반사용자
          """)
#------------------------------메뉴 합수 종료-------------

#프로그램 시작
while run: #주실행코드
    main_menu() # 위에서 만든 메인메뉴를 실행
    select = input(">>>") #키보드로 메뉴선택
    if select == "1": # 회원가입 코드
        member_add()  # 회원가입용 함수 호출



    elif select == "2": # 로그인 메뉴 선택
        member_login()  # 로그인용 함수 호출

    elif select == "3":  # 로그아웃 메뉴 선택
        member_logout()  # 로그아웃 함수 호출


    elif select == "4":  # 회원정보 수정 선택
        member_modify()  # 회원정보 수정 함수 호출

    elif select == "5": # 회원 탈퇴 선택
        member_delete() # 회원 탈퇴 함수 호출

    elif select == "9": # 프로그램 종료
        run = False
    else:
        print("잘못 입력하셨습니다.")

 #while문 종료



