# 파이썬과 mysql 병합 작업을 위한 sql 페이지

# 절차 일반적으로 system(root)계정은 개발용으로 허용하지 않는다.
# mysql에 사용할 id와 pw와 권한을 부여하고 db를 생성한다.


CREATE USER 'mbc'@'localhost' IDENTIFIED BY '1234';
# 사용자계정생성  ID     접속PC                     암호
#           'lhj'@'192.168.0.154'             '5678' ->임효정씨가 154주소로 들어옴
#           'lhj'@'192.168.0.%'(대역대)  -> 192.168.0.1~192.168.0.255 (1~255)
#           'lhj'@'%'                  ->전체 ip(외부에서도 접속됨 -> 보완에 좋지않음)
# 사용자 계정 생성은 id가 중복되어도 됨 -> 대신 접속 PC를 다중처리 할 수 있음
# CREATE USER 'mbc'@'192.168.0.%' IDENTIFIED BY '5678';
# CREATE USER 'mbc'@'%' IDENTIFIED BY 'Mbc320!!';


# 사용자 삭제
drop user 'mbc'@'localhost';

# mbc 사용자에게 lms 권한 부여
# 1. 데이터베이스 생성 -> 2. 계정에 권한을 준다
drop database lms;
create database lms default character set utf8mb4 collate utf8mb4_general_ci;
# lms 데이터베이스생성                        한국어지원 utf-8
# collate: 문자 집합에 포함된 문자들을 어떻게 비교하고 정렬할지 정의 하는 키워드
# 데이터비교시 대소문자 구분, 문자간의 정렬순서, 언어별 특수문자 처리방식 지원
# utf8m64 :문자집합
# general : 비교규칙(간단한 일반비교)
# ci : case Insensitive(대소문자 구분하지 않음)
# COLLATE utf8mb4_bin (대소문자 구분함)

# mbc라는 계정이 lms를 사용할 수 있게 권한 부여
GRANT ALL privileges on lms.* to 'mbc'@'localhost';
# 권한을 부여한다       db명.table id       접속 pc
# all privileges -> 모든권한 부여
# grant select, insert on lms.* to '알바'@'%';
#        read    create

# 권한 즉시 반영
flush privileges;

use mysql;  # mysql 최고 DB에 접속
select * from user; # mysql에 사용자 목록을 볼수 있다.
