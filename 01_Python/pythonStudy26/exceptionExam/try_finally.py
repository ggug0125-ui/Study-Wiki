# try-finally :try문 수행중 예외발생 여부세 상관없이
# 무조건 수행되는 문장!!

try : # 에외가 발생할거 같은 실행문
    f = open("foo.txt","w")
    # 이것 저것 실행문을 써

finally: # 중간에 오류가 나도 실행!! 안나도 실행!!!!
    f.close()