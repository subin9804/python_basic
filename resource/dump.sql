BEGIN TRANSACTION;
CREATE TABLE users(id INTEGER PRIMARY KEY, username TEXT, email TEXT, phone TEXT, website TEXT, regdate TEXT);
INSERT INTO "users" VALUES(1,'Kim','kim@naver.com','010-0000-0000','kim@co.kr','2024-09-17 02:38:17');
INSERT INTO "users" VALUES(2,'Park','Park@daum.net','010-2222-2222','park.co.kr','2024-09-17 02:38:17');
INSERT INTO "users" VALUES(3,'Lee','Lee@naver.com','010-3333-3333','Lee.co.kr','2024-09-17 02:38:17');
INSERT INTO "users" VALUES(4,'Lee','Cho@naver.com','010-4444-4444','Cho.co.kr','2024-09-17 02:38:17');
INSERT INTO "users" VALUES(5,'Yoo','Yoo@naver.com','010-5555-5555','Yoo.co.kr','2024-09-17 02:38:17');
COMMIT;
