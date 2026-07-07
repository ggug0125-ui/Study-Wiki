run = True
sns = []
ids = []
passwords = []
names = []
emails = []
admins = []

menu = """
엠비씨 아카데미 회원 프로그램
1. 회원가입
2. 로그인
3. 회원보기
4. 내정보수정
5. 프로그램 종료

"""

while run:
    print(menu)
    select = input("해당하는 숫자를 입력하세요 : ")
    if select == "1":
        print("회원가입 메뉴입니다.")
        sn = input("회원번호를 입력하세요 : ")
        id = input("아이디를 입력하세요 : ") #id 일 경우 중복확인을 한번 한다
        if id in ids:
            print("이미 존재하는 아이디입니다.")
            continue     # id 중복여부 물어보고 계속실행하려면 continue를 쓴다
            


