# 주민번호를 입력받아 생년월일 남녀 구분을 하는 코드
# input() 함수를 사용하면 콘솔로 데이터를 넣을 수 있다.
# 처리0: 주민번호 입력 검증 ->
# 14글자인지? 6번째에 - 유무 (주민번호인증코드가 있음 -구글검색)
# 처리1: 생년월일 추출! -> 1,3,5,6 1900년생, 나머지 2000년생
# 처리2: 주민번호 8번째 글자를 추출 -> 남여구분
# 처리3: 9~10번째 글자를 추출 -> 출생지역

print ("주민등록번호를 입력하세요!! (-포함, 14글자)")
aaa = input(">>>")

if len(aaa) == 14 :
    print("주민등록번호가 일치합니다.")
else :
    print("주민등록번호가 일치하지 않습니다.")

if aaa[6] == "-":
    print("입력하신 정보가 맞습니다.")
else:
    print("입력하신 정보가 일치하지 않습니다.")

print ("입력된 주민번호는 " + aaa + "입니다")

year = int(aaa[0:2])
month = int(aaa[2:4])
day = int(aaa[4:6])

allaaa = ""
if aaa[7] in ["1","2","5","6"]:
    allaaa = "19" + str(year)
    print("귀 하의 생년은 :" + allaaa + "년생 입니다.")
else:
    allaaa = "20" + str(year)
    print("귀 하의 생년은 :" + allaaa + "년생 입니다.")

age = 2026 - int(allaaa)
print("귀하의 나이는 " + str(age) + "세 입니다.")


gender = aaa[8]
if gender in [1,3,5,7] :
    gender = "남성"
else:
    gender = "여성"

print("귀하는 " + gender + "입니다.")

Local = ""
ssnLocal = aaa[8:10]
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
