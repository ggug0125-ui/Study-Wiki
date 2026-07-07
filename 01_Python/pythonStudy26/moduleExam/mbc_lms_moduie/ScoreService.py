
class ScoreService:
    def __init__(self):
        members = []

    def run (self):
        subrun = True
        while subrun:
            print("""
            ---------------------------------
            엠비씨 아카데미 성적관리 서비스 입니다.
            1. 성적 입력
            2. 성적 보기
            3. 성적 수정
            4. 성적 삭제
            5. 종료
            """)
            subselect = input(">>>")
            if subselect == "1":
                print("성적입력 메뉴로 진입합니다.")
                print("성적입력 메뉴를 종료합니다.")
            elif subselect == "2":
                print("성적보기 메뉴로 진입합니다.")
                print("성적보기 메뉴를 종료합니다.")
            elif subselect == "3":
                print("성적수정 메뉴로 진입합니다.")
                print("성적수정 메뉴를 종료합니다.")
            elif subselect == "4":
                print("성적삭제 메뉴로 진입합니다.")
                print("성적삭제 메뉴를 종료합니다.")
            elif subselect == "5":
                print("성적관리 서비스를 종료합니다.")
                subrun = False
            else:
                print("잘못된 번호를 입력하였습니다. ")
                print("처음부터 다시 입력하세요 ")