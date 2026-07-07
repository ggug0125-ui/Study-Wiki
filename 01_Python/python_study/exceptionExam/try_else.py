# try-else :try문 수행중 오류가 발생하면
# 오류가 발생하면 except 절을 처리하고
# 오류가 발생하지 않으면 else절이수행

try :
    age = int(input("나이를 입력하세요!!!"))

except : #except에 클래스를 넣지 않으면 모두 예외!!
    print("슷자만 입력하세요!!!")
else : # 예외발생하지 않으면 처리되는 문장
    if age <= 18 :
        print("귀하는 미성년자입니다.")
    else:
        print("환영합니다.")
        