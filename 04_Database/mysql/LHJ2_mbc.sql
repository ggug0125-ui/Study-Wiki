-- 'LHJ'@'192.168.0.%' '1021'  'lhj_mbc';
-- CREATE USER 'LHJ'@'192.168.0.%' IDENTIFIED BY '1021';

use lhj_mbc;

DROP TABLE IF EXISTS members;

CREATE TABLE members (
    id INT NOT NULL AUTO_INCREMENT,
    uid VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    name VARCHAR(50) NOT NULL,
    role ENUM('admin','manager','user') DEFAULT 'user',
    active TINYINT(1) DEFAULT 1,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    
    PRIMARY KEY (id),
    UNIQUE KEY (uid)
) ENGINE=InnoDB AUTO_INCREMENT=65 
  DEFAULT CHARSET=utf8mb4 
  COLLATE=utf8mb4_general_ci;
  
  
  





INSERT INTO members 
(uid, password, name, role, active, created_at)
VALUES
('aaaa','0000','관리자','admin',1,NOW()),
('mmmm','0000','임효정','manager',1,NOW()),
('lhj','0000','임효정','user',1,NOW()),
('user02','1111','이영희','user',1,NOW()),
('user03','1111','박민수','user',1,NOW()),
('user04','1111','최지은','user',1,NOW()),
('user05','1111','정현우','user',1,NOW()),
('user06','1111','강수진','user',1,NOW()),
('user07','1111','윤태호','user',1,NOW()),
('user08','1111','한소희','user',1,NOW()),
('user09','1111','오세훈','user',1,NOW()),
('user10','1111','신유진','user',1,NOW()),
('user11','1111','임도현','user',1,NOW()),
('user12','1111','홍지수','user',1,NOW()),
('user13','1111','서민재','user',1,NOW()),
('user14','1111','문가영','user',1,NOW()),
('user15','1111','조한결','user',1,NOW()),
('user16','1111','김하린','user',1,NOW()),
('user17','1111','박지훈','user',1,NOW()),
('user18','1111','이수민','user',1,NOW()),
('user19','1111','정다은','user',1,NOW()),
('user20','1111','최도윤','user',1,NOW()),
('user21','1111','유재석','user',1,NOW()),
('user22','1111','김태리','user',1,NOW()),
('user23','1111','박서준','user',1,NOW()),
('user24','1111','아이유','user',1,NOW()),
('user25','1111','차은우','user',1,NOW()),
('user26','1111','전지현','user',1,NOW()),
('user27','1111','송중기','user',1,NOW()),
('user28','1111','한지민','user',1,NOW());

select * from members;

SELECT *
FROM members
WHERE role IN ('admin','manager')
  AND active = 1;
SELECT DATABASE();
SHOW TABLES;
