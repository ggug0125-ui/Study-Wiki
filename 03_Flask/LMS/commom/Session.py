# commom은 로그인 상태 관리 클래스야
# 로그인한 회원 객체를 보관한다
# 전역변수대신 객체로 돌려 써
# 로그인, 로그아웃, 로그인여부, 관리자인지??

class  Session:   # __init__ 필요없음  cls로 Member를 활용하기때문에
    login_member = None    # 처음으로 현재 로그인한 겍체를 불러와야지~

    @classmethod  # 이건 객체가 돌아다니게 하는 함수야!!
    def login(cls,member):     # cls와 셋트로 구현하는거야
        cls.login_member = member  # cls를 묶어서 멤버라고 지정한겨!!!

    @classmethod
    def logout(cls,member):    # 로그인상태인 사람 로그아웃
        cls.login_member = None

    @classmethod
    def is_login(cls):          # 로그인상태니??
        return cls.login_member is not None   #cls 멤버객체야?  None 아니면 True

    @classmethod
    def is_admin(cls):           # 권한자 구분  관리자니???
        return cls.is_login() and cls.login_member.is_admin()

    @classmethod
    def is_manager(cls):         # 메니저니????
        return cls.is_login() and cls.login_member.is_manager()
    #            로그인한사람   둘다          로그인권한메니저
    #                       and 는 둘다 참 일때 참 처리하지~

