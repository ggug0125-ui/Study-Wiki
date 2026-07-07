# 회원에 관한 CRUD를 구현
# 부메뉴와 함께 run()메서드를 진행



class MemberService:
    def __init__(self):
        # 클래스 생성시 필요한 변수들.....
        # 파일명 , 멤버리스트
        members = []  # 모든회원이 들어있는 2차원 리스트

    def run(self):
        # 부메뉴 구현 메서드
        subrun = True
        while subrun:
            print("""
            -----------------------------------
            엠비씨 아카데미 회원관리 서비스 입니다.
            1. 로그인
            2. 회원가입
            3. 회원수정
            4. 회원탈퇴
            5. 로그아웃
            
            9. 회원 서비스 종료 
            """)

            subselect = input(">>>")
            if subselect == "1":
                print("로그인 메뉴로 진입합니다. ")
            elif subselect == "2":
                print("회원가입 메뉴로 진입합니다. ")
            elif subselect == "3":
                print("회원 수정 메뉴로 진입합니다. ")
            elif subselect == "4":
                print("회원 탈퇴 메뉴로 진입합니다. ")
            elif subselect == "5":
                print("로그아웃 메뉴로 진입합니다. ")
            elif subselect == "9":
                print("회원 서비스를 종료합니다. ")
                subrun = False
            else:
                print("잘못된 번호를 입력하였습니다. ")
                print("처음부터 다시 입력하세요 ")