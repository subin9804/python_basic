# Section12-1
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 생성 및 삽입

import sqlite3
import datetime

# 삽입 날짜 생성
now = datetime.datetime.now()
print('now : ', now)

now2 = now.strftime('%Y-%m-%d %H:%M:%S')
print('now2 : ', now2)
print()

# sqlite3 버전
print('sqlite3.version : ', sqlite3.version)
print('sqlite3.sqlite_version: ', sqlite3.sqlite_version)
print()

# DB 생성 & Auto Commit (Rollback)
conn = sqlite3.connect('C:/Users/subin/Desktop/python_basic/resource/database.db', isolation_level=None)

# Cursor
c = conn.cursor()
print('Cursor Type : ', type(c))


# 테이블 생성(Data Type: TEXT, NUMERIC, INTEGER, REAL, BLOB)
#c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username TEXT, email TEXT, phone TEXT, website TEXT, regdate TEXT)")

# 데이터 삽입
#c.execute("INSERT INTO users VALUES(1, 'Kim', 'kim@naver.com', '010-0000-0000', 'kim@co.kr', ?)", (now2,))
#c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES(?,?,?,?,?,?)", (2, 'Park', 'Park@daum.net', '010-2222-2222', 'park.co.kr', now2))

# Many 삽입(튜플, 리스트)
userList = (
    (3, 'Lee', 'Lee@naver.com', '010-3333-3333', 'Lee.co.kr', now2),
    (4, 'Lee', 'Cho@naver.com', '010-4444-4444', 'Cho.co.kr', now2),
    (5, 'Yoo', 'Yoo@naver.com', '010-5555-5555', 'Yoo.co.kr', now2)
)

#c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES(?,?,?,?,?,?)", userList)

# 테이블 데이터 삭제
#conn.execute("DELETE FROM users")
#print("users db deleted : ", conn.execute("DELETE FROM users").rowcount)

# 커밋: isolation_level = None일 경우 자동으로 반영(Auto Commit)
# conn.commit()

# 롤백
# conn.rollback()

# 접속 해제
conn.close()
