
import os

class ItemService:
    def __init__(self,FILE_NAME = "Items.txt"): # 클래스 시작
        self.FILE_NAME = FILE_NAME
        self.items = []
        self.session = None
        self.load_items()

    def load_items(self):
        self.items = []
        if not os.path.exists(self.FILE_NAME):
            self.save_items()
            return

        with open(self.FILE_NAME, "r" ,encoding ="utf-8") as f:
            for line in f:
                data = line.strip().split("|")
                data[0] = int(data[0])  # 번호
                data[2] = int(data[2])  # 가격
                data[3] = int(data[3])  # 수량
                data[6] = True if data[6] == "True" else False
                self.items.append(data)
            print(self.items)

    def save_items(self):
        with open(self.FILE_NAME, "w", encoding="utf-8") as f:
            for i in self.items:
                f.write(f"{i[0]}|{i[1]}|{i[2]}|{i[3]}|{i[4]}|{i[5]}|{i[6]}\n")

    def new_item(self):
        print("상품을 등록합니다.")
        no = max([i[0] for i in self.items], default=0) + 1
        name = input("상품명을 입력하세요 : ")
        price = input("상품 가격을 입력하세요 : ")
        qty = input("상품 수량을 입력하세요 : ")
        info = input("상품 설명을 등록하세요 : ")
        print("1. 주교재자료 2. 부교재자료 3. 기타자료 ")
        cat_no = input(">>>")
        if cat_no == "1":
            cate = "주교재 자료"
        elif cat_no == "2":
            cate = "부교재 자료"
        elif cat_no == "3":
            cate = "기타 자료"

        print(" 입력된 정보를 확인합니다. ")
        print("-" * 50)
        print(f"상품 명 : {name}  상품 가격 : {price}")
        print(f"상품 수량 : {qty}  상품 설명 : {info}")
        print(f"등록된 카테고리는 {cate} 입니다. ")
        print("-" * 50)

        save_True = input("저장하려면 y를 누르세요 : ")
        if save_True == "y":
            self.items.append([no, name, price, qty, info, cate, True])
        self.save_items()  # 여기에 저장
        self.load_items()
        print("상품 등록이 완료 되었습니다.")

    def item_list(self):
        print("현재 판매중인 상품입니다.")
        print("-" * 50)
        print("\n [ 교보재 리스트 ] ")
        print("-" * 50)
        for idx, i in enumerate(self.items):
            status = "판매중" if i[6] else "판매종료"
            print(f"{i[0]:5} {i[1]:5} {i[2]:5} {i[3]:5} {i[4]:5} {i[5]:5} {status:5}")
            print("-" * 50)

    def item_view(self):
        self.item_list()
        no = int(input("\n 상세 조회할 상품 번호 : "))
        for i in self.items:
            if i[0] == no:
                print(f"상품 명: {i[1]}, 상품 가격: {i[2]}")
                print(f"상품 수량: {i[3]}, 상품 설명: {i[4]}")
                print(f"카테고리 : {i[5]}, 상태 : {i[6]}")
                return

        print("존재하지 않는 상품입니다.")

    def item_update(self):
        self.item_list()
        sel = int(input("\n수정할 상품 번호 : "))
        for i in self.items:
            if i[0] == sel:
                print("수정할 내용 선택")
                print(" 1.상품명 변경 2.가격 변경 ")
                print(" 3.수량변경    4.상품 설명변경")
                subsel = input(">>>")
                if subsel == "1":
                    i[1] = input("수정할 상품명: ")
                    print(f"상품명이 {i[1]}로 변경되었습니다.")
                elif subsel == "2":
                    i[2] = input("수정할 가격 : ")
                    print(f"상품가격이 {i[2]}로 변경되었습니다.")
                elif subsel == "3":
                    i[3] = input("수정할 수량 : ")
                    print(f"상품수량이 {i[3]}로 변경되었습니다.")
                elif subsel == "4":
                    i[4] = input("수정할 상품설명 : ")
                    print(f"상품설명이 {i[4]}로 변경되었습니다.")

                else:
                    print("잘못입력하셨습니다. ")
                    return
        self.save_items()
        self.load_items()


    def item_delete(self):
        self.item_list()
        print(" 교보재 삭제 하기 ")
        sel = int(input("\n삭제할 상품 번호 : "))
        for idx, i in enumerate(self.items):
            if i[0] == sel:
                self.items.pop(idx)
                print("삭제 완료")
                break
        else:
            print("존재하지 않는 상품입니다.")
        self.save_items()
        self.load_items()




    def run(self):
        subrun = True
        while subrun:
              print("""
-----------------------------------------
             교재관리 프로그램
-----------------------------------------
1. 교보재 등록
2. 교보재 리스트 보기
3. 교보재 자세히 보기
4. 교보재 수정하기
5. 교보재 삭제하기
6. 교재관리 종료
            """)
              sel = input(">>>")

              if sel == "1":
                  self.new_item()
              elif sel == "2":
                  self.item_list()
              elif sel == "3":
                  self.item_view()
              elif sel == "4":
                  self.item_update()
              elif sel == "5":
                  self.item_delete()
              elif sel == "6":
                  break


