# 프로그램 개발자는 시작이 되는 프로그램 명을 대부분 메인으로 만든다

# 모듈을 불러오기 위해서는 import를 사용하는데
# 저장 위치가 중요하다!!!!!
# 같은 위치에 있는 py파일을 불러오려면 파일명만 쓰면된다.
# import mod1 # .py를 생략하고 파일명만 사용한다.
# import는 이미 만들어 놓은 파이썬 모듈을 사용
# print(mod1.add(4,8))
#    (파일명.매서드명(파라미터))

# print(mod1.sub(5,3))
# 파일명.메서드명으로 사용하면 코드가 길어짐
# from을 이용하면 좀더 짧게 사용가능

from mod1 import *    # ( add, sub )메서드를 붙이거나 " * " 을 붙인다 * 는 모든값이다!!!!!
#    파일명     매서드명
print(add(3,4))
print(sub(5,3))
print(__name__)

import mod2
a = mod2.Math() #a 클래스에 Math()인스턴스를 붙인다
print(a.solv(2))
