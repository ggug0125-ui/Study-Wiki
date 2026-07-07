# oop 기반의 Member 객체용
class Member:
    def __init__(self, id, uid, pw, name, role = "user", active = True):
        self.id = id
        self.uid = uid
        self.pw = pw
        self.name = name
        self.role = role
        self.active = active
        # 사용법
        # member = Member("kkw","1234","김기원","user")
        # Member객체를 member변수에 넣음

    @classmethod
    def from_db(cls, row: dict):
        #            row는 딕셔너리 타입으로
        #            row : dict(타입 명시) 힌트
        """
        DictCursor로부터 전달받은 딕셔너리 데이터를 Member 객체로 변환합니다.
        """
        if not row:   # cls로 전달된 값이 없으면
            return None
        return cls(   # db 에 있는 정보를 딕셔너리타입으로 받아와 아이디에 넣음
            id = row.get('id'),
            uid = row.get('uid'),
            pw = row.get('password'),
            name = row.get('name'),
            role = row.get('role'),
            active = bool(row.get('active'))
         )

    def is_admin(self):  # role이 어드민이야? 확인하는 메서드
        return self.role == "admin"

    def __str__(self): # member객체를 문자열로 출력할때 사용 (테스트용)
        return f"{self.name}({self.id}:{self.pw}) [{self.role}]"
