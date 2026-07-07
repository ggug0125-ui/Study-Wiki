class Member:
    def __init__(self, uid, pw, name, role="user", active=True):   #초기값
        self.uid = uid
        self.pw = pw
        self.name = name
        self.role = role
        self.active = active

    def __str__(self):                                           #프린트 처리되는용(테스트용)
        status = "활성" if self.active else "비활성"
        return f"{self.uid}|{self.name}|{self.role}|{status}"

    def to_line(self):                                  # 메모리 객체를 메모장으로 저장시 문자열 변환
        return f"{self.uid}|{self.pw}|{self.name}|{self.role}|{self.active}\n"

    @staticmethod  # 객체가 아니라 문자열 처리
    def from_line(line: str):
        line = line.strip()
        if not line:
            return None

        parts = line.split("|")
        if len(parts) != 5:
            return None

        uid, pw, name, role, active = parts

        return Member(
            uid=uid,
            pw=pw,
            name=name,
            role=role,
            active=(active == "True")
        )


    def is_admin(self):                   # 권한 처리용 메서드
        return self.role == "admin"

    def is_manager(self):
        return self.role == "manager"

