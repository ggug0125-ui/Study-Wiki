CREATE USER 'LHJ'@'localhost' IDENTIFIED BY '1021';

create database lhj_mbc default character set utf8mb4 collate utf8mb4_general_ci;
# lms 데이터베이스생성                        한국어지원 utf-8
# collate: 문자 집합에 포함된 문자들을 어떻게 비교하고 정렬할지 정의 하는 키워드
# 데이터비교시 대소문자 구분, 문자간의 정렬순서, 언어별 특수문자 처리방식 지원
# utf8m64 :문자집합
# general : 비교규칙(간단한 일반비교)
# ci : case Insensitive(대소문자 구분하지 않음)
# COLLATE utf8mb4_bin (대소문자 구분함)

# mbc라는 계정이 lms를 사용할 수 있게 권한 부여
GRANT ALL privileges on lhj_mbc.* to 'LHJ'@'localhost';
# 권한을 부여한다       db명.table id       접속 pc
# all privileges -> 모든권한 부여
# grant select, insert on lms.* to '알바'@'%';
#        read    create

# 권한 즉시 반영
flush privileges;

use mysql;  # mysql 최고 DB에 접속
select * from user; # mysql에 사용자 목록을 볼수 있다.