# 클래스는 대부분 파일명을 대문자로 만드는게 관례이다( 시작앞에 대문자!!)
# 클래스는 인스턴스를 목적으로 만듬

class Calculator: # 파일명과 클래스 명도 대문자로 시작!! (: 이면 들여쓰기해야해)
    # : (콜론이기 때문에 들여쓰기 중요함)
    # 내부에 함수(매서드)를 생성한다
    def __init__(self):
        # 초기화 매서드
        # 클래스 선언시 기본적으로 실행되는 문법
        self.result = 0 # 클래스가 생성되면서 변수를 만듬
        #self 는주소야!! 딴거없어 (스텍영역/ 힙영역) 힙역역이 클래스 두개만들어 힙영역의 주소야!
        # 인잇에 변수를 다 여기다 넣어
#------------기본 주소---------------------------------------------------

    def add(self, num):
        self.result += num    # result = result + num
        return self.result

    def sub(self, num):       # result = result - num
        self.result -= num
        return self.result

    def mul(self, num):       # result = result * num
        self.result *= num
        return self.result

    def div(self, num):       # result = result / num
        self.result /= num
        return self.result
    # 이건 함수 기능이야!!! 계산식 보기 수정 등등


# class 선언종료!! 클래스선언 밑에 들여쓰기해서 함수만들어!!!!!
# CRUD는 클래스 안쪽에 들여쓰기해서 만들어!!
cal1 = Calculator()
#변수에 객체를 연결
cal2 = Calculator()
# 클래스를 사용하려면 변수에 영역(스텍과 힙영역이 붙어 연결이됨)
# 이때 사용하는게 self
# 객체(인스턴스) 생성과 변수 연결 (self) 끝
#-------------------------------------------------------------------
# 객체.메서드(값) self 로 연결된 주소의 객체를 찾아서
# .add(5) 실행한다 -> 매서드 실행후 결과를 받음
kkwresult = cal1.add(5)
print(kkwresult)

ksbresult = cal2.add(7)
print(ksbresult)

print(cal1.sub(10))
print(cal2.mul(9))
print(cal2.div(9))

