#클래스용도로 파일을 생성하면 대문자로 시작하는게 관례이다

class FourCal:
    # pass # 아무동작 안하고 넘어감
    # 변수 선언부 __init__ 생성자~!!
    def __init__(self):  #인잇은 항상 맨처음 self는 바꿀수있어~ 근데 관례상 self쓴대
        self.first = 0
        self.second = 0
        #이것은 취약한 코드!!


    # 메서드 선언부
    # 세터와 게터를 이용해 구현함


    def setdata(self,first,second):  #값을 넣을때는 set  #값을 구할때 get~!!!
    # a.first와 a.second를 직접 가서 처리가 가능
    # 하지만 검증해서 값을 처리하는 것도 필요함
    # 데이터를 넣는 메서드를 세터라고 한다~ set~!!!!

       if first <= 0 :
           self.first = 0
       else :
           self.first = first

       if second <= 0 :
           self.second = 0
       else:
           self.second = second

    def add(self):
        result = self.first + self.second
        return result


    def div(self):
        result = self.first / self.second
        # 나누는 값이 0이면 컴퓨터는 오류를 발생시킴
        return result




a = FourCal()
# a.first = 100   #객체 변수에 바로 입력이됨
# a.second = 200  # 다이렉트로 객체변수에 입력하면 검증이안됨

a.setdata(-10,second=10)
result1 = a.add()
print(f"-10+10 : add()메서드 실행결과 :  {result1}")
print(a.first) #객체 변수에 바로 출력이됨
print(a.second)
# 위 방법은 개밯자들이 취약한 코드라고 판담한다~!! 검증 함수를 이용후 넣자~!!
# a이 변수에 FourCal() 클래스를 연결
print(type(a))
# <class '__main__.FourCal'>
# __main__ -> 모듈의 이름을 담고있는 파이썬의 내장변수
# 최상위 코드가 실행되는 환경의 이름( 주 실행코드)
# 건물에는 무조건 1층 입구가 있듯이 프로그램실행은 메인으로 판단한다~!!

class MoreFourCal(FourCal):
    #             부모객체 ( + , -,*,/)
    # 부모객체의 모든 기능을 사용하면서 추가 매서드를 만듬
    def pow(self):
        result = self.first ** self.second
        return result
        # 부모의 추가 매서드 (제곱처리)
    def div(self): #부모와 같은 메서드 명!!!
        if self.second == 0:
            #나누는 뒷값이 0이면 나눌필요도 없이 0을 리턴
            return 0
        else:
            return self.first / self.second


c = MoreFourCal()
c.add() # 부모의 더하기 매서드활용
c.pow() # 자식의 제곱처리 매서드활용

# 매서드 오버라이딩 (부모가 만든 메서드를 튜닝 할 때)
# d = FourCal()
# d.setdata(first=8,second=0)
# result = d.div()
# print(result)

e = MoreFourCal()
e.setdata(first=9,second=0)
result = e.div()  #부모에서 개선된 자식 div()를  실행함 (부모꺼쓰려면 포칼 가져오기!!!)
print(result)

# 클래스 변수(필드) : __init__ 나 일반 메서드에 바깥쪽 변수

class Family :     # 클래스 바깐에 클래스는 필드
    lastname = "김"

    # 이곳은 매서드들....
print(Family.lastname)

a = Family()
b = Family()
a.lastname = "최"
print(a.lastname)
print(b.lastname)








