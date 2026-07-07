# 회원관리용 코드를 만든다.
# C -> 회원추가
# R -> 관리자일 경우 (전제회원보기), 일반회원일경우 (로그인)
# U -> 관리자일 경우 (회원차단,암호변경문의), 일반회원(내정보 수정, 암호변경)
# D -> 회원 탈퇴

# 메뉴 구현

run = True  # 프로그램 동작중을 관리하는 변수

menu = """
========================================
       mbc 아카데미 회원관리 프로그램
========================================
1. 회원가입
2. 로그인
3. 회원보기
4. 내정보수정
5. 프로그램 종료
"""

# 사용할 리스트 변수를 생성한다.
sns = [1, 2]  #학번 사용자관리번호 중복되지 않는값 먼저만든다
ids = ["kkw", "lhj"]  # 로그인용 ID
password = ["1234", "4321"] # 로그인용 PW
name = ["관리자", "임효정"]  #사용자명
emails = ["admin@mbc.com", "lhj@mbc.com"] # 이메일주소
admins = [True,False] # 관리자 유무, 관리자: True, 일반사용지 False



while run:
    print (menu)
    select = input ("1~5 숫자를 입력하세요 : ")
    if select == "1":
        sn = input("사번을 입력하세요")
        id = input("아이디를 입력하세요")
        pw = input("암호를 입력하세요")
        name = input("이름을 입력하세요")
        email = input("이메일을 입력하세요")
        admin = False

        print("입렫된 값을 확인하시고 y를 누르면 가입됩니다")
        print("이름 : " + name)
        print("ID : " + id)
        print("PW : " + pw)
        if input("y/n : ") == "y":
            sns.append(sn)
            ids.append(id)
            password.append(pw)
            name.append(name)
            email.append(email)
            admin.append(admin)
            print("입력이 완료되었습니다.")
        else:
            print("처음부터 다시 진행하세요!!!")

    elif select == "2":
        print("로그인 메뉴에 진입하셨습니다.")
    elif select == "3":
        print("회원 정보 보기 메뉴에 진입하셨습니다.")
    elif select == "4":
        print("내정보 수정 페이지 입니다.")
    elif select == "5":
        print("회원가입프로그램이 종료되었습니다.")
        run = False
    else:
        print("1~5사이 값을 입력하세요")
