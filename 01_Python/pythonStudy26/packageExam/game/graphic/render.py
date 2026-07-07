# 만약 이곳에서 sound 디렉토리에 있는 echo.py모듈을 사용하고 싶다면??

from ..sound.echo import echo_test
#    .. 상위폴더로 이동 -> game




def render_test():
    print("render_test")
    print("graphic/render_test를 실행함")
    echo_test()
