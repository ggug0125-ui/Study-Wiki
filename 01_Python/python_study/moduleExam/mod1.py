# 모듈 학습하기
# 모듈은 파이썬 파일로 만든것을 연동하여 프로그램으로 처리한다
# 실무에서는 파일 1개로 모두 만들어 제공하는것이 아니라
# 각각 기능이 있는 파일을 빼서 클래스화 하고 매서드로 동작한다.

# Main.py  -> __name__(__main__)주실행코드 와 서비스를 연결하는 주메뉴와 메서드
# MemberService.py __name__(__MemberService__) 회원관리 클래스와 메서드
# ScorsService.py   __name__(__ScorsService__)성적관리 클래스와 매서드
# BoardService.py  __name__(__BoardService__) 게시판을 관리하는 클래스와 메서드
# ItemService.py    __name__(__ItemService__)상품을 관리하는 클래스와 메서드
# CartService.py    __name__(__CartService__)장바구니를 관리하는 클래스와 메서드

# 파이썬 확장자.py로 만든 파이썬파일은 모두 모듈로 처리가능함

def add(a, b):
    return a + b
#
def sub(a, b):
    return a - b
#
# print(add(1,4))
# print(sub(4,2))
# 터미널에 python을 실행하고
# import mod1문이 실행된다
# 당연한 결과임
# 근데 main 에서 실행하면 ?? 이중처리 모드1출력, 메일에서 출력 두개가 다 출력된다.!!
# mod1.py에서 print 2개 실행
# main.py에서 print 2개실행
# main 에서는 add와 sub 함수만 호출해서 사용하려고만 했다
# 프린트 조절   ===== >  if문   이때는 if문으로 실행을 조절해야함!!

if __name__=="__main__":  # 네임을 프린트안하려면 메인으로 if문써서 바꾼다 메인에 네임으로 들어가게된다!!
    print(add(3,4))
    print(sub(5,3))

print(__name__)  #터미널에서 dir / cd 탭 두번 / 모듈이그잼인걸 확인후 / python / import mod1 / 프린트 / mod1출력
