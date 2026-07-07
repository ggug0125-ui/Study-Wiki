# 주실행코드로 주메뉴를 담당한다.
# 외부 모듈을 호출해서 연동한다.
import MemberService #회원 관리용 클래스
import ScoreService #회원 점수관리용 클래스
import BoardService #게시판 관리용 클래스
import ItemService #상품관리용 클래스
import AdminService

run = True

def main():
    run = True
    while run:
        print(f"""
==============================
  엠비씨 아케데미 LMS 서비스입니다.
1. 회원관리
2. 성적관리
3. 자료 게시판관리
4. 교보재관리
5. 교수전용
6. 취업용 게시판

9. 종료
""")
        select = input(">>>")
        if select == "1":
            print("회원관리 서비스로 진입합니다.")
            # 회원 서비스 클래스 호출용 코드
            MemberService.MemberService().run()
            #import   .      클래스()  .   매서드()
            print("회원관리 서비스를 종료합니다.")

        elif select == "2":
            print("성적관리 서비스로 진입합니다.")
            ScoreService.ScoreService().run()
            print("성적관리 서비스를 종료합니다")

        elif select == "3":
            print("자료게시판 관리 서비스로 진입합니다")
            BoardService.BoardService().run()
            print("자료게시판 관리 서비스를 종료합니다")

        elif select == "4":
            print("교보재 관리 서비스로 진입합니다")
            ItemService.ItemService().run()
            print("교보재 관리 서비스를 종료합니다")

        elif select == "5" :
            print("교수전용 관리 서비스로 진입합니다")
            AdminService.AdminService().run()
            print("교수전용 관리 서비스를 종료합니다")

        elif select == "6" :
            print("취업용 게시판 관리 서비스로 진입합니다")

            print("취업용 게시판 관리 서비스를 종료합니다")

        elif select == "9" :
            print("엠비씨 LMS서비스를 종료합니다.")
            run = False
        else:
            print("잘못된 번호를 선택하였습니다.")
            print("다시 입력하세요 ")


if __name__ == "__main__":
    # 여러파일을 호출하기 때문에 main일때만 main()메서드를 실행
    main() #위에 만든 main()함수를 실행한다.

