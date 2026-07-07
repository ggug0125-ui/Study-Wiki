from LMS.common import Session
from LMS.domain import Member

class MemberService:

    @classmethod
    def load(cls):        # 데이터베이스 읽어오기~~~
        conn = Session.get_connection()   # 세션에 만든 메서드를 호출해~~~
        # lms DB를 가져와서 conn에 넣어라~
        # 예외 발생이 있을수 있음
        try :
            with conn.cursor() as cursor:  # db에서 가져온 객체 1줄을 cursor이라고 해
                cursor.execute('select count(*) as cnt from members')
                #              Member테이블에서 개수나온 것을 cnt변수에 넣어~
                count = cursor.fetchone()['cnt'] # 딕셔너리타입으로 cnt : 5 이렇게 표시됨
                #             .fetchone() 1개의 결과가 나올때 readone
                #             .fetchall() 여러개의 결과가 나올때 readall
                #             .fetchmany(3) 3개의 결과만 보고 싶을 때 (최상위3개)
                print(f"시스템에 현재 등록된 회원수는 {count}명 입니다.")

        except: # 예외발생 문구
            print("MemberService.load()메서드 오류 발생.....")
        finally: # 항상 출력되는 코드
            print("데이터베이스 접속 종료됨......")
            conn.close()

    @classmethod
    def login(cls):                             # 로그인 하기~~~~~~~~~~~~~~~
        print("\n[ 로 그 인 ]")
        uid = input("아이디: ")
        pw = input("비밀번호: ")
        conn = Session.get_connection()    # db 자료 가져와바~

        try:
            with conn.cursor() as cursor: # db에서 가져온 객체 1줄이랑 비교해바
                # 아이디랑 비밀번호가 일치하는 회원을 찾아바바
                sql = "select * from members where uid = %s and password = %s"
                print("spl = " + sql) # 이게뭔지 확인용이야 모르면 프린트
                cursor.execute(sql, (uid, pw))
                #                 튜플식 고정값이라 변경할수없음
                row = cursor.fetchone()

                if row:
                    member = Member.from_db(row)
                    # 계정이 비활성화인지 체크
                    if not member.active:
                        print("[알림] 비활성화된 계정입니다. 관리자에게 문의하세요.")
                        return
                    Session.set_login_member(member)
                    print(f"[성공] {member.name}님 환영합니다. 로그인이 되었습니다.")
                else:
                    print("[알림] 아이디 또는 비밀번호가 틀렸습니다.")
        except Exception as e:
            print("[알림] MemberService.login() 오류:", e)
        finally:
            conn.close()

    @classmethod
    def logout(cls):                            # 로그아웃 하기~~~~~~~~~~~~~
        if not Session.is_login():
            print("\n[알림] 현재 로그인 상태가 아닙니다.")
            return

        Session.logout()
        print("\n[성공] 로그아웃이 되었습니다. 안녕히 가세요~")

    @classmethod
    def signup(cls):                            # 회원가입 하기~~~~~~~~~~~~~~~
        if not Session.is_login():
            print("\n [ 회  원  가  입 ] ")
            uid = input("아이디 : ")
            conn = Session.get_connection()   #  DB자료 가져와바

            try:
                with conn.cursor() as cursor:
                    check_sql = "select * from members where uid = %s"  # (쿼리문)
                    # 중복체크해보자
                    cursor.execute(check_sql, (uid,))
                    # SQL 쿼리 결과에서 단 한 개의 행(row)만 튜플(tuple) 형태로 반환합니다.
                    # 호출할 때마다 다음 행으로 넘어가며, 더 이상 행이 없으면 None을 반환합니다.
                    # 딕셔너리 커서 사용 시 딕셔너리 형태로도 출력됩니다.
                    if cursor.fetchone():
                        print(" 이미 존재하는 아이디입니다. ")
                        return
                    pw = input("비밀번호: ")
                    name = input("이름: ")

                    # 데이터 삽입
                    insert_sql = "insert into members (uid, password, name) values (%s, %s, %s)" #(쿼리문)
                    cursor.execute(insert_sql, (uid, pw, name))
                    conn.commit()
                    print("[성공] 회원가입이 완료 되었습니다. 로그인을 해주세요~")

            except Exception as e:  # (쿼리문이 두개일경우 확인한다~!!)
                conn.rollback()
                # 트렌젝션 : 쿼리문이 둘다 참일때는 commit()
                #                하나라도 오류일경우 rollback()
                print(f"[알림] 회원가입 오류 발생 사유 : {e}")
            finally: conn.close()

    @classmethod
    def modify(cls):                            # 회원정보 수정 하기~~~~~~~~~~~~~~
        if not Session.is_login():
            print("\n[알림] 현재 로그인 상태가 아닙니다.")
            return
        member = Session.login_member

        print(f"[성공] 내 정보를 확인합니다. {member}")
        print("""
        [ 내 정보 수정 ] 
        1. 이름 변경           2. 비밀번호 변경
        3. 계정 비활성 및 탈퇴   0. 취소
        """)
        sel = input("선택번호 : ")
        new_name = member.name    # 변수정하기
        new_pw = member.pw         # 변수정하기
        if sel == "1":
            new_name = input("새 이름 : ")
        elif sel == "2":
            new_pw = input("새 비밀번호 : ")
        elif sel == "3":
            print("[알림] 회원 비활성화 및 탈퇴를 진행합니다.")
            cls.delete()
        else:
            return
        conn = Session.get_connection()   # 디비 자료 가져와바
        try:
            with conn.cursor() as cursor: # 한줄씩 꺼내
                sql = "update members set name = %s , password = %s where id = %s"   # 이름형식 비번형식 요런형식으로
                cursor.execute(sql, (new_name, new_pw, member.id))  # 튜풀 고정값으로
                conn.commit() # 저장해
                member.name = new_name  # 메모리세션 정보도 동기화시켜
                member.pw = new_pw      # 메모리세션 정보도 동기화시켜
                print("[성공] 회원정보 수정이 완료되었습니다.")
        finally:
            conn.close()

    @classmethod
    def delete(cls):                                # 회원 탈퇴 및 계정 비활성화
        if not Session.is_login():
            print("\n[알림] 현재 로그인 상태가 아닙니다.")
            return
        member = Session.login_member
        print("""
        [  회  원  탈  퇴  ]
        1. 완전 탈퇴  2. 계정 비활성화 
        """)
        sel = input("선택번호 : ")
        conn = Session.get_connection()  # 디비에서 회원정보 찾아바
        try:
            with conn.cursor() as cursor: # 한줄로 끄내바
                if sel == "1":
                    sql = "delete from members where id = %s"  # 자료 삭제해~~
                    cursor.execute(sql, (member.id,))  # 튜플식은 한개여도 마지막에 콤마 찍어야해~!!!!
                    print("[성공] 회원 탈퇴가 완료되었습니다. 안녕히 가세요~")
                elif sel == "2":
                    sql = "update members set active = False where id = %s"
                    cursor.execute(sql, (member.id,))
                    print("[성공] 계정을 비활성화 하였습니다. ")
                conn.commit()
                Session.logout()
        finally:
            conn.close()

# ---------------------------이건 내가 해본거야~~~~~~~~~~~~~~~~~~ 관리자계정 다시 해보기~~~~~~~

    @classmethod
    def admin_menu(cls):                            # 관리자 계정~~~~~~~~~~~~
        if not Session.is_login():
            print("\n[알림] 현재 로그인 상태가 아닙니다.")
            return

        if not Session.is_admin():
            print("[알림] 관리자 권한만 이용가능합니다.")
            return
        conn = Session.get_connection()
        while True:
            print("""
               [ 관 리 자 메 뉴 ]
               1. 회원 목록 조회
               2. 권한 변경
               0. 뒤로가기
               """)
            sel = input("선택 번호 : ")
            if sel == "1":
                pass
            elif sel == "2":
                cls.change_role()
            elif sel == "0":
                break

    @classmethod
    def change_role(cls):
        if not Session.is_admin():
            print("[알림] 관리자만 권한 변경이 가능합니다.")
            return

        conn = Session.get_connection()

        try:
            with conn.cursor() as cursor:
                uid = input("권한을 변경할 회원 아이디: ")
                sql = "select id, uid, role from members where uid = %s" # db자료에 확인
                cursor.execute(sql, (uid,))  # 한줄빼와
                row = cursor.fetchone()

                if row is None:
                    print("[알림] 해당 회원이 존재하지 않습니다.")
                    return

                print(f"현재 권한: {row['role']}")
                print("변경할 권한 (user / manager / admin)")
                new_role = input(">>> ").strip()

                if new_role not in ("user", "manager", "admin"):
                    print("[알림] 올바르지 않은 권한입니다.")
                    return

                update_sql = "update members set role = %s where id = %s"
                cursor.execute(update_sql, (new_role, row["id"]))
                conn.commit()

                print(f"[성공] {uid} 회원의 권한이 '{new_role}'로 변경되었습니다.")

        except Exception as e:
            print("[오류] 권한 변경 중 오류 발생:", e)
        finally:
            conn.close()









