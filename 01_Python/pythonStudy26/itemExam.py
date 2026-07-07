# 상품에 대한 CRUD를 구현해보자
# C 새상품등록
# R 전체상품 목록
# R 단일 상품 자세히 보기
# U 상품 수정
# D 상품 품절(매진)
# 사용할 변수  전역변수
run = True
item_names = ["노트북","모니터","마우스"]    #상품명
unit_prices = [1200000,400000,30000]   #단가
quantitys = [40,25,60]      #수량
product_infos = ["AI용 삼성 노트북","LG24인치 LED","전기종 호환 마우스"]  #상품 정보
categorys = ["가전","가전","잡화"]  # 상품 분류

# 사용할 메서드 (함수)
def new_item():
    # print("new_item() 함수 호출 완료")
    print("새상품을 등록합니다.")

    name = input("상품명: ")
    price = int(input("단가 : "))
    qty = int(input("수량 : "))
    info = input(("상품 설명 : "))
    item_add_menu()
    cat_num = input("카테고리 선택 : ")
    if cat_num == "1":
        cat = "교재"
    elif cat_num == "2":
        cat = "잡화"
    elif cat_num == "3":
        cat = "음식"
    elif cat_num == "4":
        cat = "패션"

    else:
        print("잘못된 카테고리 선택")
        return      # 새상품 추가용 실행문
    abc = input("등록한 상품의 정보가 맞습니까? (y/n) : ")
    if abc == "y":
        item_names.append(name)
        unit_prices.append(price)
        quantitys.append(qty)
        product_infos.append(info)
        categorys.append(cat)
        print("상품이 등록되었습니다.")
    else:
        print("상품이 등록되지 않았습니다.")


def item_list():
   # print("item_list() 함수 호출 완료")
    print("현재 판매중인 상품 리스트입니다.")
    print("\n [ 상품리스트 ] ")
    print("번호 / 상품명 / 가격 / 수량 / 카테고리 ")
    print("-"*40)

    for i in range(len(item_names)):
        print(f"{i} / {item_names[i]} /  {unit_prices[i]} / {quantitys[i]} / {product_infos[i]} / {categorys[i]}")



    #리스트 출력용 for item in item_names:

def item_view():
   # print("item_view() 함수 호출 완료")
    print("상품 자세히 보기")
    #상품에 대한 상세 정보 표시
    item_list()
    idx = int(input("\n 상세 조회할 상품번호 : "))
    if 0 <= idx < len(item_names):  # idx 범위 0보다 작으면 마이나스, 상품보다 많으면 초과 X
        print("\n [ 상품 상세 정보 ] ")
        print("상품 명 : ",item_names[idx])
        print("가   격 : ",unit_prices[idx])
        print("수   량 : ",quantitys[idx])
        print("설   명 : ",product_infos[idx])
        print("카테고리 : ",categorys[idx])
    else:
        print("존재하지 않는 상품입니다.")


def item_update():
    # print("item_update() 함수 호출 완료")
    print("상품 수정하기")
    #상품에 대한 내용 수정하기
    item_list()
    idx = int(input(f"수정할 상품 번호 : "))
    if 0 <= (idx) < len(item_names):

        name = input(f"변경할 상품명({item_names[idx]}) : ")
        price = input(f"변경할 가격({unit_prices[idx]}) : ")
        qty = input(f"변경할 수량({quantitys[idx]}) : ")
        info = input(f"변경할 상품 설명({product_infos[idx]}) : ")
        cat = input(f"변경할 카테고리({categorys[idx]}) : ")

        item_names[idx] = name
        unit_prices[idx] = int(price)
        quantitys[idx] = int(qty)
        product_infos[idx] = info
        categorys[idx] = cat
        print("상품 수정이 완료 되었습니다.")


    else:
        print("존재하지 않는 상품입니다.")

def item_delete():
    # print("item_delete() 함수 호출 완료")
    print("상품 삭제하기")
    # 상품 품절, 삭제하기
    item_list()
    idx = int(input("\n삭제할 상품번호 : "))
    if 0 <= idx < len(item_names):
        item_names.pop(idx)
        unit_prices.pop(idx)
        quantitys.pop(idx)
        product_infos.pop(idx)
        categorys.pop(idx)

        print("등록된 상품이 삭제되었습니다.")
    else:
        print("존재하지 않는 상품입니다.")


def item_deiete1():
    print("싱품 품절 관리 메뉴입니다.")
    item_list()
    idx = int(input("\n품절 처리할 상품번호 : "))

    if 0 <= idx < len(item_names):
        quantitys[idx] = 0

        print(f"품절 [{item_names[idx]}] 상품이 품절 처리 되었습니다.")
    else:
        print("존재하지 않는 상품입니다.")

    #메인메뉴

def main_menu():
    print("""
============================================
M B C 아카데미 쇼핑몰입니다.
    
1. 상품등록
2. 상품리스트
3. 상품자세히보기
4. 상품 수정하기
5. 상품 삭제하기
6. 상품 품절처리하기
    
9. 프로그램 종료
    
    """)
def item_add_menu():
    print("""
====== 상품 추가용 메뉴에 진입 =======
1. 교재
2. 잡화
3. 음식
4. 패션

9. 종료
    """)
#프로그램 주실행
while run:
    main_menu()  #메인메뉴 함수 호출하여 출력
    select = input("선택할 숫자를 입력하세요 : ")
    if select == "1":
        new_item()

    elif select == "2":
        item_list()


    elif select == "3":
        item_view()

    elif select == "4":
        item_update()

    elif select == "5":
        item_delete()

    elif select == "6":
        item_deiete1()

    elif select == "9":
        run = False
    else:
        print("잘못된 숫자를 입력하셨습니다.")
        print("다시 입력하세요~!!")