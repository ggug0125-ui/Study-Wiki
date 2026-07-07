class Board:
    def __init__(self, no, title, content, writer, active=True):
        self.no = no                # 글 번호
        self.title = title          # 제목
        self.content = content      # 내용
        self.writer = writer        # 작성자 아이디
        self.active = active        # 삭제여부

        #파일 저장용 직렬화
    def to_line(self):
        return f"{self.no}|{self.title}|{self.content}|{self.writer}|{self.active}\n"

        #파일 로드용 역질렬화

    @staticmethod
    def from_line(line):
        line = line.strip()
        if not line:
            return None

        parts = line.split("|")
        if len(parts) != 5:
            return None

        no, title, content, writer, active = parts
        return Board(int(no), title, content, writer, active == "True")
