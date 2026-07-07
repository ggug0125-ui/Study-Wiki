# 세션에서 db 접속도 관리하자!!!
# 현재 세션으로 상태관리를 하는데 차후에
# 프론트를 배우면 웹브라우져에서 세션을 처리한다.
# html + css + js : w3c라고 부른다. 웹표준!!!
# 차후에는 이곳이 db관리하는 connetion 영역이 될 것이다.

# 파이참에도 db를 관리하는 메뉴가 있다.
# 오른쪽 버튼에 db 선택함 -> mysql 워크벤치 대타용



import pymysql      # 터미널에 설치해야해~ 처음 시작할때~~~~ 그래야 연결됨
                    # pip install pymysql 터미널 설치 필수

class Session:
    login_member = None

    @staticmethod
    def get_connection():   # db 연결용 메서드
        print("get_connection()메서드 호출 - mysql에 접속됩니다.")

        return pymysql.connect(
            host="localhost",
            user="mbc",
            password="1234",
            db="lms",
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor
            # 딕셔너리 타입으로 처리함 (키 : 벨류)
        )
    @classmethod
    def set_login_member(cls, member):   #멤버서비스에서 로그인시 객체를 담아놈
        cls.login_member = member

    @classmethod
    def logout(cls):
        cls.login_member = None

    @classmethod
    def is_login(cls):   # 로그인 상태를 확인
        return cls.login_member is not None  #로긴했으면 참 아님 거짓

    # 추가 권한 메서드 (서비스계출에서 사용됨)
    @classmethod
    def is_admin(cls):  # 어드민이니??
        return cls.is_login() and cls.login_member.role == "admin"
        # 로그인을 했고 role 이 어드민이면 참이고 아님 거짓이야~
    @classmethod
    def is_manager(cls):
        return cls.is_login() and cls.login_member.role in ("manager", "admin")

