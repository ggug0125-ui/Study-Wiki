#LMS에 대한 테이블을 생성하고 더미데이터 입력(CRUD)
SHOW DATABASES; #LMS만 보인다.
USE LMS; # LMS데이터 베이스를 사용하겠다.

 # drop table members; # 잘못 만들었을경우 삭제

CREATE TABLE members(  #members테이블을 생성
    # 필드명     타입   옵션
	id			int auto_increment primary key,
	#          정수    자동번호생성기    기본키 (다른테이블과 연결용)
	uid 		varchar(50) not null unique,
    #           가변문자(50자) 공백비허용  유일한값
	password 	varchar(255) not null,
	name 		varchar(50) not null,
	role 		enum('admin','manager','user') default 'user',
    #           열거타입(괄호안에 글자만 허용)        기본값은 user
    active 		boolean default true,
    #			불린타입           기본값 / true = 1, false = 0
    created_at datetime default current_timestamp
    # 생성일     날짜 시간타입       기본값은 시스템시간
    );
    
# 더미데이터 입력
insert into members (uid, password, name, role, active)
values ('kkw','1234','김기원','admin',true);
insert into members (uid, password, name, role, active)
values ('lhj','5678','임효정','manager',true);
insert into members (uid, password, name, role, active)
values ('kdg','1111','김도균','user',true);
insert into members (uid, password, name, role, active)
values ('ksb','2222','김수빈','user',true);
insert into members (uid, password, name, role, active)
values ('kjy','3333','김지영','user',true);            #여러개 추가시 ctrl + shift + enter하기!!!!!!

# 더이데이터 출력
select * from members; #전체 출력

# 로그인 할 때
select * from members where uid='kkw' and password = '1234' and active = true;   #조건부 출력

# 더미데이터 수정
update members set password = '1111' where uid = 'kkw';
#                   패스워드를 1111 로 바꾼다       아이디 kkw

# 회원삭제
delete from members where uid = 'kkw';
# 회원 비활성화
update members set active = false where uid = 'kkw';

drop table scores;
create table scores (
	id			int auto_increment primary key,
    member_id	int not null,
    korean		int not null,
    english		int not null,
    math		int not null,
    total 		int not null,
    avgrage 	float not null,
    grade		char(1) not null,
    #           a,b,c등급 
    creater_at  datetime default current_timestamp,
    
    foreign key (member_id) references members(id)
    # 외래키생성    내가갖은필드와     연결      테이블에있는 필드랑
);

# 후보키 : 공백이 없고, 유일해야 되는 필드들을 말한다.(학번,id,email,핸드폰번호,주민번호 후보키들...)
# primary key 는 기본키로 공백이 없고, 유일해야 하고, 인덱싱이 되어 있는 옵션
# 인덱싱 : db에서 빠른 찾기를 위한 옵션
# 외래키(foreign key) : 다른테이블과 연결이 되는 키!!
# 외래키는 자식이고 기본키는 부모
# members가 부모임으로 kkw 계정이 있어야 scores 테이블에 kkw 점수를 넣을수있다.
# members테이블의 id 와 scores 테이블의 member_id 타입일치는 필수

insert into scores (member_id, korean, english, math, total, avgrage, grade)
values (2,99,99,99,297,99,'A');
insert into scores (member_id, korean, english, math, total, avgrage, grade)
values (3,88,88,88,264,88,'B');
insert into scores (member_id, korean, english, math, total, avgrage, grade)
values (4,77,77,77,231,77,'C');
insert into scores (member_id, korean, english, math, total, avgrage, grade)
values (5,66,66,66,198,66,'F');
insert into scores (member_id, korean, english, math, total, avgrage, grade)
values (6,80,80,80,240,80,'B');

select * from scores; -- 전체 출력

# 기본 정보 조회 (inner join)
# 성적 데이터가 존재하는 회원만 조회합니다. 이름,과목,점수,평균,등급을 가져오는 쿼리
select
	m.name as 이름,
    #      as 제목이름변경(영어->한글로)
    m.uid as 아이디,
    s.korean as 국어,
    s.english as 영어,
    s.math as 수학,
    s.total as 총점,
    s.avgrage as 평균,
    s.grade as 등급
from members m
# aliasing (별칭): member m 처럼 테이블 이름 뒤에 한글자 별칭을 주면 쿼리가 훨씬 간결해짐
join scores s on m.id = s.member_id;
# on 조건: m.id = s.member_id와
# 같이 두 테이블을 연결하는 핵심 키 (PK-FK)를 정확히 지정.

delete from scores where member_id = 2;

# 성적이 없는 회원도 포함 조회 (left jion)
# 성적표가 아직 작성되지 않는 회원까지 모두 포함하여 명단을 만들때 사용합니다. 성적이 없으면 null로 표시됩니다.

select
	m.name as 이름,
    m.role as 역할,
    s.avgrage as 평균,
    s.grade as 등급,
	ifnull(s.grade,'미산출') as 상태  #성적이 없으면 '미산출'표시
from members m
left join scores s on m.id = s.member_id;

# 게시판 생성
drop table boards;
create table boards (
	id 		int auto_increment primary key,
    member_id int not null,
    title varchar(200) not null,
    content text not null,
    created_at datetime default current_timestamp,
    
    foreign key (member_id) references members(id)
);

insert into boards (member_id,title, content)
values (3,'제목1','내용1');
insert into boards (member_id,title, content)
values (4,'제목4','내용4');
insert into boards (member_id,title, content)
values (4,'제목5','내용5');
insert into boards (member_id,title, content)
values (5,'제목6','내용6');

select * from boards;

# 게시글 목록조회 (inner join)
select
	b.id as 글번호,
    b.title as 제목,
    m.name as 작성자, -- members 테이블에서 가져옴
    b.created_at as 작성일
from boards b
inner join members m on b.member_id = m.id
order by b.created_at DESC; -- 최신글 순으로 정렬

# 특정 사용자의 글만 조회 (where절 조합)
select
	b.title,
    b.content,
    m.name as 작성자, -- members 테이블에서 가져옴
    b.created_at
from boards b
join members m on b.member_id = m.id
where m.uid = 'lhj'; -- 특정 아이디를 가진 유저의 글만 필터링

# 관리자용 : 통계 조회 (group by 조합)
select
	m.name,
	m.uid,
    count(b.id) as 작성글수 # group by와 셋트
from members m
left join boards b on m.id = b.member_id
group by m.id;

# 작성자 이름으로 검색하기 (like 활용)
select
	b.id as 글번호,
    b.title as 제목,
	m.name as 작성자,
    b.created_at as 작성일
from boards b
inner join members m on b.member_id = m.id
where m.name like '%효정%'
#            포함하는
order by b.created_at desc;

# where m.mane like '%검색어%' or b.title like '%검색어%'

#===============여기까지 수업내용======= 밑에꺼는 복붙한거임=========





drop table items;
CREATE TABLE items (
    id        INT AUTO_INCREMENT PRIMARY KEY,
    code      VARCHAR(20) NOT NULL UNIQUE,
    name      VARCHAR(100) NOT NULL,
    category  ENUM('잡화','음료','IT','도서') NOT NULL,
    price     INT NOT NULL,
    stock     INT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);


INSERT INTO items (code, name, category, price, stock)
VALUES ('KKK','아이스커피','음료', 5000, 60);
INSERT INTO items (code, name, category, price, stock)
VALUES ('QQQ','맥심커피','음료', 1000, 30);
INSERT INTO items (code, name, category, price, stock)
VALUES ('WWW','노트북','IT', 500000, 20);
INSERT INTO items (code, name, category, price, stock)
VALUES ('EEE','모니터','IT', 300000, 50);
INSERT INTO items (code, name, category, price, stock)
VALUES ('TTT','파이썬','도서', 30000, 80);
INSERT INTO items (code, name, category, price, stock)
VALUES ('AAA','공책','잡화', 1000, 55);
INSERT INTO items (code, name, category, price, stock)
VALUES ('SSS','데이터베이스','도서', 23000, 70);

SELECT * FROM items;

drop table orders;
CREATE TABLE orders ( # 주문용 테이블
    id        INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT NOT NULL,
    status    ENUM('PAID','REFUND_REQ','REFUNDED','CANCELED') DEFAULT 'PAID',
    #               결재완료   환불대기        환불됨       취소됨
    total_price INT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (member_id) REFERENCES members(id)
);

INSERT INTO orders (member_id, status, total_price)
VALUES (3,'PAID',60000);
INSERT INTO orders (member_id, status, total_price)
VALUES (4,'REFUND_REQ',70000);
INSERT INTO orders (member_id, status, total_price)
VALUES (5,'REFUNDED',80000);
INSERT INTO orders (member_id, status, total_price)
VALUES (6,'CANCELED',90000);

SELECT * FROM orders;


drop table order_items;
CREATE TABLE order_items (  # 주문내역 테이블
    id        INT AUTO_INCREMENT PRIMARY KEY,
    order_id  INT NOT NULL,
    item_id   INT NOT NULL,
    qty       INT NOT NULL,
    price     INT NOT NULL,

    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (item_id) REFERENCES items(id)
);

INSERT INTO order_items (order_id, item_id, qty, price)
VALUES (1, 1, 12, 50000);
INSERT INTO order_items (order_id, item_id, qty, price)
VALUES (2, 3, 20, 80000);
INSERT INTO order_items (order_id, item_id, qty, price)
VALUES (3, 6, 15, 80000);
INSERT INTO order_items (order_id, item_id, qty, price)
VALUES (4, 7, 8, 88600);

SELECT * FROM order_items;

# "누가 무엇을 샀는가?" (3개 테이블 조인)
# 회원(members), 주문(orders), 주문 상세(order_items)를 연결하여 고객별 구매 이력을 뽑아내는 예제입니다.
SELECT 
    m.name AS 구매자,
    o.id AS 주문번호,
    o.status AS 상태,
    oi.price AS 구매단가,
    oi.qty AS 수량,
    (oi.price * oi.qty) AS 결제금액
FROM members m
JOIN orders o ON m.id = o.member_id
JOIN order_items oi ON o.id = oi.order_id
ORDER BY o.created_at DESC;

# "어떤 상품이 가장 많이 팔렸나?" (집계 함수와 조인)
# items와 order_items를 조인하여 상품별 판매 통계를 내는 예제입니다. 재고 관리할 때 필수적인 쿼리
SELECT 
    i.name AS 상품명,
    i.category AS 카테고리,
    SUM(oi.qty) AS 총판매량,
    SUM(oi.price * oi.qty) AS 총매출액
FROM items i
LEFT JOIN order_items oi ON i.id = oi.item_id
GROUP BY i.id
ORDER BY 총판매량 DESC;
# 여기서 LEFT JOIN을 쓴 이유는 한 번도 팔리지 않은 상품
# 도 목록에 나오게 해서 판매 부진 상품을 파악하기 위함입니다.

# "카테고리별 매출 분석" (조건부 조인)
# 특정 카테고리(예: '음료')에서 발생한 매출만 뽑아보고 싶을 때 사용합니다.
SELECT 
    o.id AS 주문번호,
    i.name AS 상품명,
    o.total_price AS 전체주문금액,
    o.created_at AS 주문일시
FROM orders o
JOIN order_items oi ON o.id = oi.order_id
JOIN items i ON oi.item_id = i.id
WHERE i.category = '음료' AND o.status = 'PAID';

# 조인할 때 이것만은 꼭 기억하세요!
# 1:N 관계 파악: members(1)와 orders(N)처럼
# 데이터가 늘어나는 방향을 이해하면 어떤 테이블을 기준으로 삼을지 정하기 쉽습니다.

# 다중 조인: 조인은 2개뿐만 아니라 3개, 4개 
# 그 이상도 JOIN 문을 계속 이어서 붙일 수 있습니다. (마치 기차 놀이처럼요!)

# 성능 최적화: 조인을 많이 할수록 DB가 힘들어합니다. 
# 그래서 자주 조인되는 member_id 같은 외래키에는 인덱스(Index)가 자동으로 걸려 성능을 보조합니다.


# Outer Join(특히 LEFT OUTER JOIN)**은 
# "연결된 데이터가 없더라도, 왼쪽 기준 테이블의 정보는 무조건 다 보여달라"고 할 때 사용합니다

# 성적이 입력되지 않은 학생 명단 뽑기
# INNER JOIN을 쓰면 성적이 있는 학생만 나오지만, 
# 성적표를 아직 안 만든 학생까지 포함한 전체 학생 명부를 만들 때는 LEFT JOIN이 필수입니다.
SELECT 
    m.name AS 학생명,
    m.uid AS 아이디,
    IFNULL(s.average, 0) AS 평균점수,
    CASE WHEN s.id IS NULL THEN '미응시' ELSE '완료' END AS 시험상태
FROM members m
LEFT JOIN scores s ON m.id = s.member_id
WHERE m.role = 'user'; -- 학생 권한인 사람만

# 게시글을 한 번도 쓰지 않은 유저 찾기
# 커뮤니티 활성화를 위해 활동이 없는 유저를 파악하고 싶을 때 사용합니다.
SELECT 
    m.name, 
    m.uid, 
    m.created_at AS 가입일
FROM members m
LEFT JOIN boards b ON m.id = b.member_id
WHERE b.id IS NULL; -- 게시글 데이터가 없는 사람만 필터링

# 판매된 적 없는 상품 목록 (재고 관리)
# 어떤 상품이 인기 있는지 아는 것도 중요하지만, 한 번도 안 팔린 재고 상품을 파악하는 것도 중요하죠.
SELECT 
    i.code,
    i.name AS 상품명,
    i.stock AS 현재재고,
    i.price AS 가격
FROM items i
LEFT JOIN order_items oi ON i.id = oi.item_id
WHERE oi.id IS NULL; -- 주문 상세 내역에 한 번도 등장하지 않은 상품


# Inner vs Outer Join 한눈에 비교
# 양쪽 다 데이터가 있어야 함 / 교집합 (데이터가 누락될 수 있음) / 관련 있는 데이터만 깔끔하게 볼 때
# 왼쪽은 무조건, 오른쪽은 있으면 연결 / 왼쪽 테이블 전체 (오른쪽 없으면 NULL) / 누락된 데이터나 전체 목록을 확인할 때

# 환불 요청 고객 및 상품 정보 조회쿼리
SELECT 
    m.name AS 고객명,
    m.uid AS 아이디,
    o.id AS 주문번호,
    i.name AS 상품명,
    oi.qty AS 수량,
    (oi.price * oi.qty) AS 환불예정금액,
    o.created_at AS 주문일시,
    o.status AS 주문상태
FROM orders o
INNER JOIN members m ON o.member_id = m.id
INNER JOIN order_items oi ON o.id = oi.order_id
INNER JOIN items i ON oi.item_id = i.id
WHERE o.status = 'REFUND_REQ'  -- 상태가 '환불 요청'인 것만 필터링
ORDER BY o.created_at DESC;    -- 최신 주문부터 정렬

# orders ↔ members: 주문한 사람이 "누구"인지 이름을 알기 위해 조인했습니다.
# orders ↔ order_items: 주문 번호 하나에 상품이 여러 개 있을 수 있으므로, 상세 내역을 가져오기 위해 조인했습니다.
# order_items ↔ items: 상세 내역에는 상품 ID만 있으므로, 실제 "상품 이름"을 알기 위해 조인했습니다.
# WHERE o.status = 'REFUND_REQ': 전체 주문 중 환불이 필요한 데이터만 골라냈습니다.

# "카테고리별로 환불 요청이 얼마나 들어왔는지" 
# 궁금하다면 이렇게 그룹화(GROUP BY)를 해볼 수 있습니다.
SELECT 
    i.category AS 카테고리,
    COUNT(o.id) AS 환불요청건수,
    SUM(oi.price * oi.qty) AS 총환불금액
FROM orders o
JOIN order_items oi ON o.id = oi.order_id
JOIN items i ON oi.item_id = i.id
WHERE o.status = 'REFUND_REQ'
GROUP BY i.category;

# 회원 종합 정보(쇼핑 + 성적) 대시보드 쿼리
# **쇼핑 정보(총 구매액)**와 **학습 정보(성적 등급)**를 한눈에 보여주는 일종의 "종합 마이페이지"
# 이 쿼리는 members 테이블을 중심으로 orders(쇼핑)와 scores(성적)를 동시에 조인해야 합니다. 
# 이때 쇼핑 이력이나 성적이 없는 회원도 누락되지 않도록 **LEFT JOIN**을 사용하는 것이 핵심입니다.

SELECT 
    m.uid AS 아이디,
    m.name AS 이름,
    m.role AS 역할,
    IFNULL(s.grade, 'N/A') AS 성적등급,
    IFNULL(s.average, 0) AS 평균점수,
    COUNT(DISTINCT o.id) AS 총주문건수,
    IFNULL(SUM(oi.price * oi.qty), 0) AS 총구매금액,
    CASE WHEN m.active = TRUE THEN '활동중' ELSE '휴면' END AS 상태
FROM members m
LEFT JOIN scores s ON m.id = s.member_id
LEFT JOIN orders o ON m.id = o.member_id AND o.status = 'PAID'
LEFT JOIN order_items oi ON o.id = oi.order_id
GROUP BY 
    m.uid, 
    m.name, 
    m.role, 
    s.grade, 
    s.average, 
    m.active; -- SELECT에 등장한 모든 비집계 컬럼을 그룹에 추가
# MySQL 설정에서는 GROUP BY를 쓸 때, 집계 함수(SUM, COUNT 등)를 
# 쓰지 않은 모든 컬럼은 반드시 GROUP BY 절에 적어주거나, 집계 함수로 감싸야 합니다.

# 서브쿼리로 미리 계산하기 (성능 & 가독성 추천)
# 실무에서 데이터가 많아질 때 가장 선호하는 방식입니다. 
# **"구매 금액"**만 따로 계산해서 가져오면 GROUP BY 복잡도가 확 줄어들고 에러에서도 자유로워집니다.
SELECT 
    m.uid AS 아이디,
    m.name AS 이름,
    IFNULL(s.grade, 'N/A') AS 성적등급,
    IFNULL(s.average, 0) AS 평균점수,
    IFNULL(p.total_spent, 0) AS 총구매금액,
    IFNULL(p.order_count, 0) AS 주문건수
FROM members m
LEFT JOIN scores s ON m.id = s.member_id
LEFT JOIN (
    -- 주문 금액을 미리 계산하는 가상 테이블
    SELECT 
        o.member_id, 
        COUNT(DISTINCT o.id) AS order_count,
        SUM(oi.price * oi.qty) AS total_spent
    FROM orders o
    JOIN order_items oi ON o.id = oi.order_id
    WHERE o.status = 'PAID'
    GROUP BY o.member_id
) p ON m.id = p.member_id;


