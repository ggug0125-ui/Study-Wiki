# Database26
데이터베이스학습용(mysql)

my sql 설치를 진행한다.
https://dev.mysql.com.downloads/mysql (LTS버전을 선택한다.)

mysql 설치중 오류가 발생하면 vs code 라이브러리 설치
구글검색 : visual c++ Redistributable v14(vc_redist.x64.exe)필요

mysql 관련 프로그램을 설치한다.
https://dev.mysql.com.downloads/workbench/

```
데이터베이스 : 자료를 24시간 365일동안 보관하며 서비스를 제공함
DBMS : 데이터베이스 프로그램 (오라클 / MYSQL / MARIADB / SQLITE .... )
SQL : Structured(구조화된) Query(질의) Language(언어) 표준화된 문법
  정의어(DDL: Data Definition Language)
   데이터베이스,테이블,사용자,뷰,인덱스,스키마 생성/수정/삭제
   생성 : CREATE DATABASE / CREATE TABLE / CREATE USER
   수정 : ALTER DATABASE / ALTER TABLE / ALTER USER
   삭제 : DROP DATABASE / DROP TABLE / DROP USER
   이름변경 : RENAME TABLE / RENAME USER
   보기 : SELECT

  조작어(DML: Data Manipulation Language)
   데이터베이스 테이블에 자료 관리용
   C(자료생성) : INSERT INTO 테이블명(필드명들) VALUES (값들)
   R(찾아옴) : SELECT 필드명 FROM 테이블 WHERE 조건
   U(자료수정) : UPDATE 테이블명 SET(필드명=값) WHERE 조건
   D(자료삭제) : DELETE FROM 테이블 WHERE 조건

  제어어(DCL: Data Control Language)
   데이터의 보안, 무결성, 데이터회복, 병행수행 등...(데이터관리목적)
   ROLLBACK : 트렌젝션 복귀
   COMMIT : 트렌젝션 저장 (트렌젝션 : 일괄작업)
   GRANT : 권한 부여(사용자에게 관리자가 테이블 및 기능에 권한 부여)
   REVOKE : 권한 삭제   
```
