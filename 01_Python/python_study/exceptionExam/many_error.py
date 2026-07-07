# 예외가 이것 저것 날꺼같다 (여러개 오류)
# try 문 안에서 여러개의 오류를 처리한다
try :
    4/0
    a = [1 , 2]
    print(a[3])


# except ZeroDivisionError as e :
#     print(e)
#     print("0으로 나눠지는 예외가 발생함!!")
#
# except IOError as e :
#     print(e)
#     print("리스트 인덱스 범위 초과")

except (ZeroDivisionError, IndexError) as e :
    print(e)
    print("0으로 나눴거나 리스트 범위 초과 예외발생!!")
    print("예외 발생시 담당자에게 문의 하세요 :000-0000-0000")

