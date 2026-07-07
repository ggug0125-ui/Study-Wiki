
run = True # while 문 프로그램 구동중
board_no = []  #중복되지 않는 유일한 값, not null
board_title = [] #게시글의 제목
board_content = [] # 게시글의 내용
board_writer = []  # 글쓴이
board_password = [] #게시글의 암호(수장,삭제용)
board_hit = [] # 좋아요
board_visitcount = [] #조회 수

# 주메뉴
menu = """
=====================================
엠비씨 아카데미 비회원 게시판입니다.

1. 게시글 등록
2. 게시글 리스트 보기
3. 게시글 자세히 보기
4. 게시글 수정하기
5. 게시글 삭제하기
6. 게시판 프로그램 종료
"""

while run:
    print(menu)
    select = input ("1 ~ 6 까지 입력하세요 : ")
    if select == "1":
        print("새 게시글을 작성합니다.")
        title = input("제목 : ")
        content = input("내용 : ")
        writer = input("작성자 : ")
        password = input("비밀번호 : ")

        print(f"제목 : {title}, 내용 : {content}")
        print(f"작성자 : {writer}, 비밀번호 : {password}")
        choose = input ( " 저장하려면 y를 누르세요 : ")
        if choose == "y":
            board_title.append(title)
            board_content.append(content)
            board_writer.append(writer)
            board_password.append(password)

            no = len(board_no) + 1
            board_no.append(no)
            board_hit.append(0)
            board_visitcount.append(0)

            print(f"{no}번의 게시글이 등록 되었습니다.")
        else:
            print("게시글이 등록되지 않았습니다.")

    elif select == "2":
        print("[게시글 전체 목록 출력]")
        print("*****************************************")
        print("번호\t  제목\t  작성자\t  내용\t  조회수\t")
        print("*****************************************")

        if len(board_no) == 0:
            print("등록된 게시글이 없습니다.")
            continue

        for i in range(len(board_no)):
            print(f"{board_no[i]}\t{board_title[i]}\t{board_writer[i]}\t{board_content[i]}\t{board_visitcount[i]}")
    elif select == "3":
        print("**게시글 자세히 보기**")

        bno = int(input("게시글 번호 : "))
        if bno in board_no:
            print("게시글을 찾았습니다.")

            idfff = board_no.index(bno)  #인덱스번호
            #print(f"idfff : {idfff}")


            board_visitcount[idfff] += 1

            print("#"*30)
            print(f"번호 : {board_no[idfff]}")
            print(f"제목 : {board_title[idfff]}")
            print(f"내용 : {board_content[idfff]}")
            print(f"작성자 : {board_writer[idfff]}")
            print(f"조회수 : {board_visitcount[idfff]}")
            print(f"좋아요 : {board_hit[idfff]}")
            print("#"*30)

            if input("좋아요 누르기 (y) : ") == "y":
                board_hit[idfff] += 1
                print("좋아요가 1개 추가되었습니다.")
            else:
                print("아쉽네요. 다음에 더 좋은 게시글이 되겠습니다.")
        else:
            print("해당번호의 게시글이 없습니다.")


    elif select == "4":
        no = int(input("게시글 번호를 입력하세요 : "))
        pw = (input("게시글 암호를 입력하세요 : "))
        if no in board_no:
            idxxx = board_no.index(no)

            if board_password[idxxx] == pw:
                board_title[idxxx] = input("새 제목 : ")
                board_content[idxxx] = input("새 내용 : ")
                print("게시글이 수정되었습니다.")


    elif select == "5":
        print("[게시글 삭제]")
        no = int(input("게시글 번호 : "))
        pw = (input("게시글 암호 : "))
        if no in board_no:
            idfff = board_no.index(no)

            if board_password[idfff] == pw:
                board_no.pop(idfff)
                board_title.pop(idfff)
                board_content.pop(idfff)
                board_writer.pop(idfff)
                board_password.pop(idfff)
                board_hit.pop(idfff)
                board_visitcount.pop(idfff)
                print("게시글이 삭제되었습니다.")
            else:
                print("암호가 틀렸습니다.")
        else:
            print("게시글 번호가 없습니다.")

    elif select == "6":
        print("[비회원 게시판 프로그램을 종료합니다.")
        run = False

    else:
        print("잘못 입력하셨습니다.")






