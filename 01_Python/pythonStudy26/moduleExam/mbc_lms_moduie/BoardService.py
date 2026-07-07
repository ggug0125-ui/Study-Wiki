class BoardService:
    def __init__(self):
        members = []

    def run(self):
        subrun = True
        while subrun:
            print("""
            -----------------------------------------
            엠비씨 아카데미 자료 게시판 관리 서비스 입니다.
            1. 게시글 등록
            2. 게시글 리스트 보기
            3. 게시글 자세히 보기
            4. 게시글 수정하기
            5. 게시글 삭제하기
            6. 게시판 프로그램 종료
            """)
            subselect = input(">>>")
            if subselect == "1":
                print("게시글 등록 메뉴로 진입합니다.")
                print("게시글 등록 메뉴를 종료합니다.")
            elif subselect == "2":
                print("게시글 리스트 보기 메뉴로 진입합니다.")
                print("게시글 리스트 보기 메뉴를 종료합니다.")
            elif subselect == "3":
                print("게시글 자세히 보기 메뉴로 진입합니다.")
                print("게시글 자세히 보기 메뉴를 종료합니다.")
            elif subselect == "4":
                print("게시글 수정 메뉴로 진입합니다.")
                print("게시글 수정 메뉴를 종료합니다.")
            elif subselect == "5":
                print("게시글 삭제 메뉴로 진입합니다.")
                print("게시글 삭제 메뉴를 종료합니다.")
            elif subselect == "6":
                print("엠비씨 아카데미 자료 게시판 관리서비스를 종료합니다.")
                subrun = False
            else:
                print("잘못된 번호를 입력하였습니다. ")
                print("처음부터 다시 입력하세요 ")
