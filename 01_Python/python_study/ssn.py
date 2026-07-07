# 주민번호를 입력받아 생년월일 남녀 구분을 하는 코드
# input() 함수를 사용하면 콘솔로 데이터를 넣을 수 있다.
# 처리0: 주민번호 입력 검증 ->
# 14글자인지? 6번째에 - 유무 (주민번호인증코드가 있음 -구글검색)
# 처리1: 생년월일 추출! -> 1,2,5,6 1900년생, 나머지 2000년생
# 처리2: 주민번호 8번째 글자를 추출 -> 남여구분
# 처리3: 9~10번째 글자를 추출 -> 출생지역


print("주민번호를 입력하세요!!(-포함 14자)")
ssn = input(">>>")
# 입력된 주민번호 검증 코드

if len(ssn) == 14 : #키보드로 입력된 문자열이 14자?
    print("주민번호 14글자가 잘 입력 되었습니다.")
else :
    print("주민번호 14글자가 잘못 입력되었습니다.")
    exit(0)

if ssn[6] == "-" :
    print ("주민번호 7번째 구문자 인식완료")
else:
    print ("주민번호 7번째 구문자가 입력되지 않음")
    print ("프로그램을 처음부터 다시 실행하세요")
    exit(0)


print("입력된주민번호 : " +ssn)

# 주민번호 앞 6자리를 생년월일로 추출 -> 1,2,5,6 1900년생
# 나머지는 2000년생

year = ssn[0:2] #생년
month = ssn[2:4]
day = ssn[4:6]

fullyear = ""  #if 안쪽에서 변수를 만들면 버그가 생길수있음 미리 변수만들어놓기
# ""null 처리용

if ssn[7] in ["1","2","5","6"] :
    fullyear = "19" + year
else:
    fullyear = "20" + year

print("귀하의 생년은 : " + fullyear + "년생 입니다.")


#나이계산
age = 2026 - int(fullyear)

print("귀하의 나이는 " + str(age) +  "세 입니다.") #문자+숫자+문자는 출력오류

#                            print는 문자열 + 숫자로 출력오류가 발생
#                                    문자열로 변환(강제타입변환) -> str(age)
# 주민번호 8번째 숫자가 1,2,5,7이면 남자, 여자
gender = "" #성별 null 변수 선언

if ssn[7] in ["1","3","5","7"] :     #in 리스트안에 있는걸 비교
    gender = "남성"                  # = 은 값을 넣기
elif ssn[7] == "9" :                # == 동일값찾기
    gender = "외계인"
else :
    gender = "여성"

print("귀하는 " + gender + "로 판단됩니다.")

# 8~9번째
#서울 00-08 부산 09-12 인천13-15
#경기 16-25 강원 26-34 충청 35-47
#전라 48-66 경상 67-91 제주 92-95
Local = ""
ssnLocal = ssn[8:10]   # 출생지 코드가 추출
if int(ssnLocal) <= 8 :
    local = "서울"
elif int(ssnLocal) <= 12 :
    local = "부산"
elif int(ssnLocal) <= 15 :
    local = "인천"
elif int(ssnLocal) <= 25 :
    local = "경기"
elif int(ssnLocal) <= 34 :
    local = "강원"
elif int(ssnLocal) <= 47:
    local = "충청"
elif int(ssnLocal) <= 66 :
    local = "전라"
elif int(ssnLocal) <= 91:
    local = "경상"
elif int(ssnLocal) <= 95:
    local = "제주"
elif int(ssnLocal) <= 99:
    local = "그 외"

print ("당신의 출생지는 " + local + "입니다.")


