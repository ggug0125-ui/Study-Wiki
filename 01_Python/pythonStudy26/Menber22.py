from random import choice

run = True
login_user = None

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

sns = [1, 2, 3, 4]
ids = ["abc","def","ghi","admin"]
passwords = ["1234", "4321", "1492", "0000"]
names = ["홍길동", "임효정", "김동동", "관리자"]
emails = ["abc@mbc.com", "def@mbc.com", "ghi@mbc.com", "jjj@mbc.com"]
admins = [False, False, False, True]

while run:
    print (menu)
    select = input ("해당하는 메뉴의 숫자를 입력하세요 : ")
    if select == "1":
        print("** 회원가입 메뉴입니다 **")
        sn = input("사번을 입력하세요 : ")
        id = input("아이디를 입력하세요 : ")

        if id in ids:
            print("이미 존재하는 아이디입니다")
            continue


        pw = input("암호를 입력하세요 : ")
        name = input("이름을 입력하세요 : ")
        email = input("이메일을 입력하세요 : ")

        print('입력된 정보를 확인하시고 "YES/NO" 를 입력하세요')
        print("회원번호 : " + sn)
        print("ID : " + id)
        print("Password : " + pw)
        print("Name : " + name)
        print("Email : " + email)


        if input("YES/NO : " ) == "YES":
            sns.append(sn)
            ids.append(id)
            passwords.append(pw)
            names.append(name)
            emails.append(email)
            admins.append(False)
            print("회원가입이 완료 되었습니다.")
        else:
            print("회원가입이 취소 되었습니다.")


    elif select == "2":
        print("**로그인메뉴 입니다**")
        id = input("아이디 : ")
        pw = input("비밀번호 : ")

        if id in ids:
            idx = ids.index(id)
            if passwords[idx] == pw :
                login_user = idx
                print(f"{names[idx]}님 로그인 성공")

                if admins[idx]:
                    print("관리자 계정입니다.")

                else:
                    print("일반 회원계정입니다.")

            else:
                print("비밀번호가 틀렸습니다.")
        else:
            print("존재하지 않는 아이디입니다.")


    elif select == "3":
        if login_user is None :
            print("로그인 후 이용 가능합니다.")
            continue  #맞으면 내려와 틀리면 위로 올라가


        #관리자
        if admins[login_user]:
            print("\n[전체 회원 목록]")
            for i in range(len(ids)):
                print(f"{i+1}.{names[i]}. {ids[i]}.{emails[i]}.{admins[i]}")
        else:
            #일반회원
            print("\n[내정보]")
            print(f"이름 : {names[login_user]}")
            print(f"아이디 : {ids[login_user]}")
            print(f"이메일 : {emails[login_user]}")

    elif select == "4":
        if login_user is None :
            print("로그인 후 이용 가능합니다.")
            continue
        print("\n내정보 수정")
        print("1. 이름 변경")
        print("2. 이메일 변경")
        print("3. 비밀번호 변경")

        choice = input("선택 : ")

        if choice == "1":
           names[login_user] = input("새 이름 : ")
           print("이름 변경 완료 : " + names[login_user] + "으로 변경되었습니다.")

        elif choice == "2":
            emails[login_user] = input("새 이메일 : ")
            print("이메일 변경 완료 : " + emails[login_user] + "으로 변경되었습니다.")

        elif choice == "3":
            passwords[login_user] = input("새 비밀번호 : ")
            print("비밀번호 변경 완료 : " + passwords[login_user] + "으로 변경되었습니다.")

        else:
            print ("잘못된 선택")

    elif select == "5":
        print("프로그램을 종료합니다")
        run = False
    else:
        print("1~5 사이 숫자를 입력하세요")

