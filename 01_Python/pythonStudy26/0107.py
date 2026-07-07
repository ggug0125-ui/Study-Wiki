from Menber22 import login_user

run = True
login_user = None
menu = """
========
mbc
========
1.회원가입
2.로그인
3.회원보기
4. 내정보수정
5. 프로그램 종료
"""

sns = [1,2]
ids = ["aaa","bbb"]
passwords = ["0000","1111"]
names = ["관리자","임효정"]
emails = ["aaa@mbc.com","bbb@mac.com"]
admins = [True,False]

while run:
    print(menu)
    select = input("숫자입력하시오")
    if select == "1":
        print("회원가입")
        sn = input("사번입력하시오")
        id = input("아이디를 입력하시오")

        if id in ids:
            print("이미 존재하는 아이디입니다.")
            continue
        pw = input("암호를 입력하시오")
        name = input ("이름을 입력하세요")
        email = input("이메일을 입력하세요")

        print('입력된 정보 확인 y/n 입력하시오')
        print("회원번호 : " + sn)
        print("ID : " + id)
        print("password: " + pw)
        print("name : " + name)
        print("email : " + email)

