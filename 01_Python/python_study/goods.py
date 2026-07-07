from pure_eval.my_getattr_static import slot_descriptor

run = True
session = None

menu = """
==================================
M B C market 입니다.
==================================
1. 회원가입 [로그인]
2. market으로 이동
5. 프로그램 종료

"""
loginmenu = """
----------------------------------
MBC 회원가입 메뉴입니다.
----------------------------------
1. 로그인
2. 회원가입
3. 회원정보 보기
4. 회원수정
5. 회원탈퇴

9. 회원관리메뉴 종료
"""
loginmenu2 = """
============
1. 판매자
2. 구매자
3. 관리자
4. 메뉴 나가기
============

"""
goodsmenu = """
***********************************
MARKET GOODS 
***********************************
1. 상품등록 [판매자 전용]
2. 상품리스트 전제보기
3. 상품 자세히보기
4. 상품 수정하기 [판매자 전용]
5. 재고현황

9. market 나가기

"""
sns = [1]
ids = ["ggug01"]
pws= ["0000"]
names = ["임효정"]
emails = ["ggug01@mbc.com"]
# sellers = []
# buyers = []
# admin  = [True]
groups = ["admin"]

#================================
goods_nos = [1] #상품번호
goods_lists = ["운동화"] #상품
goods_counts = ["10"] #상품갯수
goods_prices = ["100,000"] #상품가격
totals = [] #총갯수
stock = [] #재고
basket = [] #장바구니

while run:
    print(menu)
    select = input("해당번호를 입력하세요 : ")
    if select == "1":
        print("회원가입 [로그인]메뉴로 이동합니다.")
        subRun = True
        while subRun:
            print(loginmenu)
            select = input("해당번호를 입력하세요 : ")
            if select == "1":
                if session is not None:
                    print(f"이미 로그인중입니다.\t현재 로그인중인 아이디는 {session} 입니다.")
                    continue
                print("로그인을 하세요")

                id = input("아이디를 입력하세요 : ")
                if id in ids:
                    idx = ids.index(id)
                    pw = input("비밀번호 : ")
                    if pw in pws[idx]:
                        print("로그인되었습니다.")
                        session = idx # 로그인 성공시 로그인한 인덱스를 세션에 넣음
                        continue
                    else:
                        print("비밀번호가 잘못입력되었습니다.")
                else:
                    print("아이디가 잘못입력되었습니다.")

            elif select == "2":
                print("회원가입 메뉴입니다")
                subRun = True
                while subRun:
                    print(loginmenu2)
                    subselect = input("해당번호를 입력하세요 : ")
                    if subselect == "1":
                        print("판매자로 회원가입을 시작합니다.")

                        id = input("아이디를 입력하세요 : ")
                        pw = input("비밀번호를 입력하세요 : ")
                        email = input("이메일을 입력하세요 : ")
                        seller = input("판매자로 가입합니다(y/n) : ")
                        if seller == "y":

                            print(f"아이디 : {id},\t비밀번호 : {pw},\t이메일: {email}")
                            print(f"당신은 : seller 으로 가입이 완료되었습니다.")
                            ids.append(id)
                            pws.append(pw)
                            emails.append(email)
                            groups.append("seller")

                        else:
                            print("가입이 취소 되었습니다.")

                    elif subselect == "2":
                        print("구매자로 회원가입을 시작합니다.")

                        id = input("아이디를 입력하세요 : ")
                        pw = input("비밀번호를 입력하세요 : ")
                        email = input("이메일을 입력하세요 : ")
                        buyer = input("구매자로 가입합니다(y/n) : ")
                        if buyer == "y":
                            print(f"아이디 : {id},\t비밀번호 : {pw},\t이메일: {email}")
                            print(f"당신은 : buyer으로 가입이 완료되었습니다.")
                            ids.append(id)
                            pws.append(pw)
                            emails.append(email)
                            groups.append("buyer")
                        else:
                            print("가입이 취소 되었습니다.")

                    elif subselect == "3":
                        print("관리자로 회원가입을 시작합니다.")

                        id = input("아이디를 입력하세요 : ")
                        pw = input("비밀번호를 입력하세요 : ")
                        email = input("이메일을 입력하세요 : ")
                        admin = input("관리자로 가입합니다(y/n) : ")
                        if admin == "y":
                            print(f"아이디 : {id},\t비밀번호 : {pw},\t이메일: {email}")
                            print(f"당신은 : admin 으로 가입이 완료되었습니다.")
                            ids.append(id)
                            pws.append(pw)
                            emails.append(email)
                            groups.append("admin")
                        else:
                            print("가입이 취소 되었습니다.")
                    elif subselect == "4":
                        print("메인화면으로 돌아갑니다.")
                        break

                    else:
                        print("잘못된번호가 입력되었습니다.")


            elif select == "3":
                print("회원 정보를 출력합니다.")
                print("---------------------------")
                print(" [ 회원목록 ] ")

                for i in range(len(ids)):
                    print(f"아이디: {ids[i]} , 비밀번호 : {pws[i]}, 이메일: {emails[i]} , 등급 : {groups[i]}")



            elif select == "4":
                print("회원 수정 메뉴입니다.")
                if session is None:
                    print("로그인 후 이용하세요 ")

                else:
                    print("수정할 정보를 입력하세요")
                    idx = ids.index(session)
                    ids[idx] = input("수정할 아이디: ")
                    pws[idx] = input("수정할 비밀번호: ")
                    emails[idx] = input("수정할 이메일: ")
                    session = ids[idx]
                    print(f"수정된 아이디: {ids[idx]}, 수정된 비밀번호: {pws[idx]}")
                    print(f"수정한 이메일: {emails[idx]}")

                    print("수정이 완료되었습니다.")
            elif select == "5":
                print("회원 탈퇴 메뉴입니다.")
                if session is None:
                    print("로그인 후 이용하세요 ")
                else:
                    print("회원탈퇴를 진행합니다.")
                    idx = ids.index(session)

                    print(f"\t아이디 : {ids[idx]}, 비밀번호 : {pws[idx]}")
                    print(f"이메일 : {emails[idx]}")
                    choose = input ("탈퇴를 원하면 (y/n) : ")
                    if choose == "y":
                        sns.pop(idx)
                        ids.pop(idx)
                        pws.pop(idx)
                        emails.pop(idx)
                        print("회원탈퇴가 완료되었습니다.")
                    else:
                        print("잘못된 입력입니다.")
                        break
            else:
                print("회원 탈퇴가 취소되었습니다.")
                break

    elif select == "2":
        print("market으로 이동합니다.")
        subRun = True
        while subRun:
            print(goodsmenu)
            subselect = input("해당번호를 입력하세요 : ")

            if subselect == "1":
                print("판매자의 상품등록 메뉴입니다.")
                if session is None :
                    print("로그인후 이용하세요")
                    continue
                elif groups[session] == "seller":
                    print("판매자입니다. 상품을 등록하세요")
                    goods_no = input("상품번호를 입력하세요: ")
                    goods_list = input("상품명을 입력하세요 : ")
                    goods_count = input("상품의 수량을 입력하세요 : ")
                    goods_price = input("상품의 가격을 입력하세요 : ")

                    print(f" 상품번호 : {goods_no}, 상품명 : {goods_list}")
                    print(f" 상품수량 : {goods_count}, 상품금액 : {goods_price}")
                    seif = input("입력한 정보가 맞습니까? (y/n) : ")
                    if seif == "y":
                        goods_nos.append(goods_no)
                        goods_lists.append(goods_list)
                        goods_counts.append(goods_count)
                        goods_prices.append(goods_price)

                        print("상품이 등록되었습니다.")
                    else:
                        print("상품이 등록되지 않았습니다.")
                        print("처음부터 다시 입력하세요.")

                else:
                    print("판매자가 아닙니다.")
            elif subselect == "2":
                print("등록된 상품을 전체보기 합니다.")
                print("======================================")
                print("[ 상 품 리 스 트 - 전체보기 ]")

                for i in range(len(goods_nos)):
                    print(f"상품번호 : {goods_nos[i]}, 상품명 : {goods_lists[i]}, 상품수량 : {goods_counts[i]}, 상품금액 : {goods_prices[i]}")

            elif subselect == "3":
                print("선택된 상품을 자세히 보기 합니다.")
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                print("[ 상 품 자 세 히 보 기 ]")

                no = int(input("상품번호를 입력하세요 : " ))

                if no in goods_nos:
                    idx = goods_nos.index(no)
                    print(f"상품번호 : {goods_nos[idx]}")
                    print(f"상품명 : {goods_lists[idx]}")
                    print(f"상품수량 : {goods_counts[idx]}")
                    print(f"상품금액 : {goods_prices[idx]}")

                else:
                    print("등록된 상품이 없습니다.")

            elif subselect == "4":
                if session is None :
                    print("로그인후 이용하세요")
                    continue
                elif groups[session] == "seller":
                    print("판매자입니다. 상품을 수정하세요")
                    no = input("수정할 상품번호를 입력하세요 : ")

                    if no in goods_nos:
                        print("상품이 있습니다.")
                        idx = goods_nos.index(no)

                        print(f"상품번호 : {goods_no[idx]}")
                        print(f"상품명 : {goods_lists[idx]}")
                        print(f"상품수량 : {goods_counts[idx]}")
                        print(f"상품금액 : {goods_prices[idx]}")

                        goods_lists[idx] = input("수정할 상품명 : ")
                        goods_counts[idx] = input("수정할 상품 수량 : ")
                        goods_prices[idx] = input("수정할 상품 금액 : ")

                        print("등록된 상품이 수정되었습니다.")
                    else:
                        print("잘못입력하셨습니다.")
                else:
                    print("등록된 상품이 없습니다.")
            elif subselect == "5":
                print("재고수량 관리 메뉴입니다. ")
        else:
            print(" 상위로 올라갑니다.")


























