from LMS.common.session import Session  # 로그인정보와 DB정보 가지고있음
from LMS.domain.Board import Board  # oop 보드 객체


class BoardService:
    @classmethod
    def run(cls):
        if not Session.is_login():
            print("로그인후 이용가능합니다.")
            return
        while True: # 주메뉴 반복메뉴
            print(f"\n ====== MBC 게시판 ({Session.login_member.name}접속중..)  ====== \n")
            cls.list_board()  # 리스트 전제보기
            print("1. 글 쓰기")
            print("2. 글 상세보기 (수정/삭제 가능,관리자,작성자만 가능하게만들기)")
            print("3. 뒤로가기")
            sel = input(">>>")
            if sel == "1":
                cls.write_board()
            elif sel == "2":
                cls.view_detail()
            elif sel == "0":
                break

    @classmethod   # join은 select 문에 쓴다~!!
    def list_board(cls):
        print("\n" + "=" * 60)
        print(f"{'번호':<5} | {'제목':<25} | {'작성자':<10} | {'작성일'}")
        print("-" * 60)

        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                # members 테이블과 JOIN하여 작성자 이름(name)을 가져옵니다.
                sql = """
                        SELECT b.*, m.name FROM boards b
                        JOIN members m ON b.member_id = m.id
                        ORDER BY b.id DESC \
                        """
                cursor.execute(sql)
                datas = cursor.fetchall()
                for data in datas:
                    # 날짜 형식 처리 (YYYY-MM-DD 형식으로 출력)
                    date_str = data['created_at'].strftime('%Y-%m-%d')
                    print(f"{data['id']:<5} | {data['title']:<25} | {data['name']:<10} | {date_str}")
        finally:
            conn.close()
        print("=" * 60)

    @classmethod
    def write_board(cls):
        print("\n ---- 새 글 작성 --- ")
        title = input("제목 : ")
        content = input("내용 : ")
        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                sql = "insert into boards (member_id, title, content) values (%s, %s, %s)"
                cursor.execute(sql, (Session.login_member.id, title, content))
                conn.commit()
                print("글이 성공적으로 등록되었습니다.")
        finally:
            conn.close()


    @classmethod
    def view_detail(cls):
        board_id = input("조회할 글 번호 : ")
        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                sql = """
                        SELECT b.*, m.name, m.uid
                        FROM boards b
                        join members m ON b.member_id = m.id
                        WHERE b.id = %s
                        """
                cursor.execute(sql, (board_id,))
                row = cursor.fetchone()
                if not row:
                    print("존재하지 않는 글 번호입니다.")
                    return
                print("\n" + "*" * 40)
                print(f"제목 : {row['title']}")
                print(f"작성자: {row['name']} ({row['uid']})")
                print(f"작성일: {row['created_at']}")
                print("-" * 40)
                print(row['content'])
                print("*" * 40)

                #본인이 쓴 글인 경우만 수정/삭제 메뉴 노출
                if row['member_id'] == Session.login_member.id:
                    print("1. 수정  2. 삭제  0. 목록으로")
                    sub_sel = input("선택 : ")
                    if sub_sel == "1":
                        cls.update_board(board_id)
                    elif sub_sel == "2":
                        cls.delete_board(board_id)
        finally:
            conn.close()

    @classmethod
    def update_board(cls, board_id):
        new_title = input("수정할 제목: ")
        new_content = input("수정할 내용: ")
        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                sql = "UPDATE boards SET title = %s, content = %s WHERE id = %s"
                cursor.execute(sql, (new_title, new_content, board_id))
                conn.commit()
                print("게시글 수정이 완료되었습니다.")
        finally:
            conn.close()
    @classmethod
    def delete_board(cls, board_id):
        confirm = input("게시글을 정말 삭제하시겠습니까? (y/n): ")
        if confirm.lower() != "y": return
        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                sql = "DELETE FROM boards WHERE id = %s"
                cursor.execute(sql, (board_id,))
                conn.commit()
                print("게시글이 삭제 되었습니다.")
        finally:
            conn.close()


