# 대부분 프로그래밍에서 1번이 되는 (start) 파일을 main 으로 만듬
# 목표 mbc아카데미 LMS(학사관리(학생관리,성적관리,상담내역,게시글,교수(관리자)) 프로그램을 만들어 보자
# 회원관리 : 시스템 담당자, 교수(학생정보), 행정직원(등록금납부), 학생(점수), 게스트(비회원게시판), 학부모(학생성적 출력)
# 성적관리 : 교수가 성적을 등록, 수정가능 삭제는 안됨 , 성적 전체 보기
#           행정담당자가 학기마다 백업 (이전후 삭제)
#           학생은 개인 성적 일람, 성적 출력
#           게스트는 학교 소개 페이지 열람
#           학부모는 학생의 자녀학사관리(등록금납부및 휴학처리등등)
# 게시판 : 회원제, 비회원제, 문의사항, Q/A
# 필요한 변수

run = True  # 메인메뉴용 while
#subRun = True # 보조메뉴용 while
session = None # 로그인한 사용자의 인덱스를 기억하는것 (로그인중 (상태확인))

# 필요한 리스트
# 회원에 대한 리스트
sns = [1] # 회원에 대한 번호
ids = ["kkw"] # 아이디에 대한 리스트
passwords= ["1234"] # 암호에 대한 리스트
names = ["김기원"]
emails = ["kkw@mbc.com"]
admin = [True]
group = ["admin"] # 회원등급
login_user = None
# admin (관리자), stu(학생), guest(손님) ....

# 성적에 대한 리스트
pythonScores = []   # 파이썬 점수 들
databaseScores = [] # 데이터베이스 점수 들
wwwScores = []      # 프론트 점수 들
totalScores = []    # 총점 들
avgScores = []      # 평균 들
gradeScores = []    # 등급 들
stuIdx = []        # 학생의 인덱스(학번) <-> 회원의 sns


# 게시판에 대한 리스트
board_no = []      # 게시물의 번호
board_title = []   # 게시물의 제목
board_content = [] # 게시물의 내용
board_writer = []  # 게시물의 작성자 <-> 회원의 sns

# 메뉴 구성
mainMenu = """
==================================
엠비씨 아카데미 LMS에 오신걸 환영합니다.
==================================

1. 로그인 (회원가입)
2. 성적관리
3. 게시판
4. 관리자 메뉴
9. 프로그램 종료

"""

memberMenu = """
----------------------------------
회원관리 메뉴입니다.

1. 회원가입
2. 로그인
3. 회원보기
4. 내정보 수정
5. 회원탈퇴

9. 회원관리 메뉴 종료

"""

scoreMenu = """
----------------------------------
성적관리 메뉴입니다.

1. 성적 입력 (교수전용)
2. 성적 전체보기 (교수전용)
3. 성적 수정 (교수전용)
4. 성적 백업 (행정직원전용)

9. 성적 관리 메뉴 종료
"""

boardMenu = """
----------------------------------
회원제 게시판 입니다.

1. 게시글 등록
2. 게시글 전체보기
3. 게시글 자세히보기
4. 게시글 수정
5. 게시글 삭제

9. 
"""

# 주 실행문 구현
while run:
    print(mainMenu)  # 메인 메뉴 출력용
    select = input("해당번호를 입력하세요 : ") # 인풋은 무조건 문자
    if select == "1":
        print("로그인(회원가입) 메뉴입니다")

        subRun = True
        while subRun: #부메뉴 반복용
            print(memberMenu) #회원관리메뉴

            subSelect = input("해당번호를 입력하세요 : ") #회원 부메뉴 선택값을 subSelect에 넣음

            if subSelect == "1":
                print("회원가입 메뉴로 진입합니다.")
                sn = input("사번을 입력하세요 : ")
                id = input("아이디를 입력하세요 : ")

                if sn in ids:
                    print("이미 존재하는 아이디입니다.")
                    continue
                pw = input("암호를 입력하세요 : ")
                name = input("이름을 입력하세요 : ")
                email = input("이메일을 입력하세요 : ")

                print("아래의 입력된 정보를 확인하시고 y/n를 입력하세요 : ")
                print("회원번호 : "+ sn)
                print("ID : "+ id)
                print("Password : "+ pw)
                print("Name : "+ name)
                print("Email : "+ email)

                if input("y/n: ") == "y":
                    sns.append(sn)
                    ids.append(id)
                    passwords.append(pw)
                    names.append(name)
                    emails.append(email)
                    admin.append(False)
                    print("회원 가입이 완료 되었습니다.")
                else:
                    print("회원 가입이 취소 되었습니다.")


            elif subSelect == "2":
                print("로그인 메뉴로 진입합니다.")
                id = input("아이디 : ")
                pw = input("비밀번호 : ")

                if id in ids:
                    idx = ids.index(id)
                    if passwords[idx] == pw:
                        login_user = idx
                        print(f"{names[idx]}님 로그인 성공")


                        if admin[idx] == True :
                            print("관리자 계정입니다.")
                        else:
                            print("일반 회원 계정입니다.")
                    else:
                        print("비밀번호가 틀렸습니다.")
                else:
                    print("존재하지 않는 아이디입니다.")


            elif subSelect == "3":
                print("회원 조회 메뉴로 진입합니다.")
                if login_user is None:
                    print("로그인 후 이용 가능합니다.")
                    continue
                if admin[login_user]:
                    print("\n[ 전체 회원 목록 ]")
                    for i in range(len(ids)):
                        print(f"{i+1}.{ids[i]}.{names[i]}.{emails[i]},{admin[i]}")
                else:
                    print("\n[내 정보 보기]")
                    print(f"이름 : {names[login_user]}")
                    print(f"아이디 : {ids[login_user]}")
                    print(f"이메일 : {emails[login_user]}")


            elif subSelect == "4":
                if login_user is None:
                    print("로그인 후 이용 가능 합니다.")
                    continue

                print("회원 정보 수정 메뉴로 진입합니다.")
                print("1. 이름 변경 ")
                print("2. 이메일 변경 ")
                print("3. 비밀번호 변경 ")

                choice = input("선택 : ")
                if choice == "1":
                    names[login_user] = input("변경할 이름을 등록하세요 : ")
                    print("이름이 변경되었습니다." + names[login_user])
                elif choice == "2":
                    emails[login_user] = input("변경할 이메일을 입력하세요 : ")
                    print("이메일이 변경되었습니다." + emails[login_user])
                elif choice == "3":
                    passwords[login_user] = input("변경할 비밀번호를 입력하세요 : ")
                    print("비밀번호가 변경되었습니다." + passwords[login_user])
                else:
                    print("선택한 번호를 확인하세요 (해당번호가 없습니다.)")


            elif subSelect == "9":
                print("회원 관리 메뉴를 종료합니다.")
                subRun = False #회원 while문 종료

            else : # 1,2,3,4,9 외 다른 키를 넣을경우
                print("잘못된 메뉴를 선택하였습니다.")


    if select == "2":
        print("성적관리 메뉴 입니다.")
        subRun = True
        while subRun:
            print(scoreMenu)
            select = input("해당하는 번호를 입력하세요 : ")
            if select == "1":
                print("학생의 성적을 입력합니다.")
                if login_user is None:
                    print("로그인 후 이용 가능합니다.")
                    continue
                if admin[login_user]:
                    sn = int(input("학번을 입력하세요 : "))
                    name = input("이름을 입력하세요 : ")
                    pythonScore = int(input("python 점수를 입력하세요 : "))
                    databaseScore = int(input("database 점수를 입력하세요 : "))
                    wwwScore = int(input("프론트 점수를 입력하세요 : "))

                    print("입력한 정보를 확인합니다.")
                    print(f"학번: {sn}, 이름: {name}")
                    print(f"python 점수 : {pythonScore}, database 점수 : {databaseScore}, 프론트 점수 : {wwwScore}")


                    if input("저장하려면 y/n: ") == "y":
                        sns.append(sn)
                        names.append(name)
                        pythonScores.append(pythonScore)
                        databaseScores.append(databaseScore)
                        wwwScores.append(wwwScore)
                        totalScore = pythonScore + databaseScore + wwwScore
                        avgScore = totalScore / 3
                        totalScores.append(pythonScore + databaseScore + wwwScore)
                        avgScores.append(totalScore / 3)

                        if avgScore >= 90:
                            gradeScores = "A"
                        elif avgScore >= 80:
                            gradeScores = "B"
                        elif avgScore >= 70:
                            gradeScores = "C"
                        else:
                            gradeScores = "f"

                        print("당신의 학점은 : " + gradeScores + "입니다.")
                    else:
                        print("저장되지 않았습니다.")
                        print("처음부타 다시 입력하세요")

                else:
                    print("학번이 잘못되었습니다.")

            elif select == "2":
                print("성적 전제보기 메뉴입니다.")
                print("=============================")
                print(" 성 적 목 록 ")

                for i in range(len(stuIdx)):
                    print("--------------------------------------------")
                    print("학번 : " + str(i+1) + " 이름 : " + names[i])
                    print("python 점수: " + str(pythonScores[i]))
                    print("date 점수: " + str(databaseScores[i]))
                    print("프런트 점수: " + str(wwwScores[i]))
                    print(f"총점 :  {totalScores[i]}, 평균 :  {avgScores[i]}")

                else:
                    print("등록된 학번이 없습니다.")



