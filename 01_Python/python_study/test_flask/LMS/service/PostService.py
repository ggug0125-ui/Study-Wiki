import os
import uuid

from click import command

from LMS.common import Session

class PostService:
    @staticmethod
    def save_post(member_id, title, content, files=None, upload_folder='upload/'):      # 게시글 첨부파일 등록,첨부파일포함
        """게시글과 첨부파일을 동시에 저장 (트렌젝션 처리)"""
        conn = Session.get_connection() # 디비저장
        try:
            with conn.cursor() as cursor: # 디비 상담원 연결
                sql_post = "INSERT INTO posts (member_id, title, content) VALUES (%s, %s, %s)" # 쿼리문 만들어
                cursor.execute(sql_post, (member_id, title, content)) # sql을 디비에 넣어
                post_id = cursor.lastrowid # 게시글번호 post_id라는 변수만들어서  lastrowid-> 방금 저장한게시글 번호

                if files: # 첨부파일 있을때
                    for file in files: # 파일 하나씩 가져와
                        if file and file.filename != '': # 파일 그리고 파일이름이 비어있지않는걸 처리
                            origin_name = file.filename # 파일에 파일 이름가져와
                            ext = origin_name.rsplit('.', 1)[1].lower() # 파일이름에 확장자만 꺼내 (lower() 소문자로바꺼)
                            save_name = f"{uuid.uuid4().hex}.{ext}" #중복방지코드야!! 파일이름 같을시 렌덤하게 이름을 새로만들어
                            file_path = os.path.join(upload_folder, save_name) # 저장할 폴더와 새 파일이름을 붙여
                            file.save(file_path) # 파일을 디비에 저장해

                            sql_file = """INSERT INTO attachments (post_id, origin_name, save_name, file_path) 
                                          VALUES (%s, %s, %s, %s)"""
                            cursor.execute(sql_file, (post_id, origin_name, save_name, file_path))
                conn.commit() #저장 확정
                return True
        except Exception as e:
            print(f"Error saving post: {e}")
            conn.rollback()
            return False
        finally:
            conn.close()

    @staticmethod
    def get_posts():                                            #  게시글 목록 첨부파일개수 함께 조회
        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                sql = """
                        select p.*, m.name as write_name,
                               (select count(*) from attachments where post_id = p_id) as file_count
                        from posts p 
                        join members m on p.member_id = m.id
                        order by p.created_at desc
                """
                # 포스트테이블 전체에서 m.mane을 작성자이름이라 할꺼야
                # 지금 보고있는 게시글 p.id에 붙은 파일갯수를 세어~
                # 포스트스는 p라 하고
                # 멤버스테이블 m이라하고 포스트스멤버아이디와 멤버아이디가 같은 것을 가져와
                # 최신글순으로 정렬해
                cursor.execute(sql) # sql문 실행
                return cursor.fetchall() # 결과 전부 가져와
        finally:
            conn.close()

    @staticmethod
    def get_post_detail(post_id):                                # 게시글 상세 조회 첨부파일포함
        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute("update posts set view_count = view_count + 1 where id = %s" , (post_id,))
                # 조회수 증가 뷰카운트 +1 -> 튜플식 전달로 , 필요
                sql_post = """
                        select p.*, m.name as write_name
                        from posts p
                        join members m on p.member_id = m.id
                        where p.id = %s
                """
                # 포스트테이블에서 m.nane를 작성자이름으로 할꺼야
                # 포스트테이블을 p라고 하고
                # 게시글의 member_id 와 회원의 id가 같은 것을 연결한다
                # 그래서 작성자 이름을 가져온다
                # 그리고 특정 게시글 번호(p.id = %s) 하나만 조회한다

                cursor.execute(sql_post, (post_id,)) # 쿼리문 실행해서 디비에 넣어
                post = cursor.fetchone() # 한줄만 가져와

                cursor.execute("select * from attachments where post_id = %s", (post_id,))
                #                               첨부파일있는  포스트아이디를 특정값에 넣어
                files = cursor.fetchall()  # 이글에 붙어있는 첨부파일을 다가져와

                conn.commit()
                return post,files
        finally:
            conn.close()

    @staticmethod
    def delete_post(post_id, upload_folder='upload/'):   # 게시글 삭제 및 첨부파일 파일 삭제
        # 업로드 파일에 저장된 폴더에서 POST_id를 이용해 삭제하는 함수
        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute("select save_name from attachments where post_id = %s", (post_id,))
                # 이게시글에 붙어있는 첨부파일들의 저장된 이름을 가져와
                files = cursor.fetchall() # 파일이 여려개일수있으니 전부가져와
                for f in files: # 하나씩 반복
                    file_path = os.path.join(upload_folder, f['save_name'])
                    # 실제파일경로 만들기              폴더와 파일이름을 조인해
                    if os.path.exists(file_path): # 실제파일경로가 있는지 조회해~
                        os.remove(file_path) # 서버에서 삭제해
                sql = "delete from posts where id = %s" # 디비도 삭제해야지~
                cursor.execute(sql, (post_id,)) # 해당글 삭제해~
                conn.commit() # 저장해
                return True
        except Exception as e:
            print(f"Delete Error: {e}")
            conn.rollback()
            return False
        finally:
            conn.close()

    @staticmethod
    def update_post(post_id, title, content, files=None, upload_folder='upload/'):
        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute("update posts set title = %s, content = %s where id = %s" , (title, content, post_id))

                if files and any(f.filename != '' for f in files):
                    cursor.execute("select save_name from attachments where post_id = %s", (post_id,))
                    old_files = cursor.fetchall()
                    for oid in old_files:
                        old_path = os.path.join(upload_folder, oid['save_name'])
                        if os.path.exists(old_path):
                            os.remove(old_path)
                    cursor.execute("delete from attachments where post_id = %s", (post_id,))
                    for file in files:
                        if file and file.filename != '':
                            origin_name = file.filename
                            ext = origin_name.rsplit('.', 1)[1].lower()
                            save_name = f"{uuid.uuid4().hex}.{ext}"
                            file_path = os.path.join(upload_folder, save_name)
                            file.save(file_path)

                            cursor.execute("""
                                    insert into attachments (post_id, origin_name, save_name, file_path)
                                    values (%s, %s, %s, %s)
                            """, (post_id, origin_name, save_name, file_path))
            conn.commit()
            return True
        except Exception as e:
            print(f"Update Error: {e}")
            conn.rollback()
            return False
        finally:
            conn.close()































