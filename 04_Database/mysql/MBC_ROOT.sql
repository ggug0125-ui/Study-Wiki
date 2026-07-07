-- 파일 첨부용 게시판을 사용하기 위해 DB를 새로 생성한다.

create database mbc default character set utf8mb4 collate utf8mb4_general_ci;  -- 디비생성
show databases; -- 디비 리스트 보여줘
use mbc; -- mbc db 사용할께

-- 사용할 계정 생성 및 권한 부여
drop user 'kkk'@'192.168.0.%'; -- 이미 있거나 잘못 만들면 삭제
create user 'kkk'@'192.168.0.%' identified by '1234';
--           ID     접속권한PC                    암호alter

grant all privileges on mbc.* to 'kkk'@'192.168.0.%';
-- 권한 부여 모든권한        디비명. 모든테이블 아이디 접속권한
flush privileges; -- 즉시적용