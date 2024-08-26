# Section04-3
# 파이썬 데이터 타입(자료형)
# 리스트, 튜플

# 리스트(순서O, 중복O, 수정O, 삭제O)
# 선언

a = []
b = list()
c = [1, 2, 3, 4]

# 자료형이 달라도 리스트형 가능
d = [10, 100, 'Pen', 'Banana', 'Orange"']
e = [10, 100, ['Pen', 'Banana', 'Orange']]

# 인덱싱
print(d[3])
print(d[-2])
print(d[0] + d[1])
print(e[2][1])
print(e[-1][-2])

# 슬라이싱
print(d[0:3])
print(e[2][1:3])

# 연산
print(c + d)
print(c * 3)
print(str(c[0]) + 'hi')

# 리스트 수정, 삭제
c[0] = 77
print(c)

c[1:2] = [100, 1000, 10000]
print(c)
c[1] = ['a', 'b', 'c']
print(c)

del c[1]
print(c)
del c[-1]
print(c)

print()
print()

# 리스트 함수
y = [5, 2, 3, 1, 4]
print(y)
y.append(6)
print(y)
y.sort()
print(y)
y.reverse()
print(y)
# 2번 인덱스에 7을 넣기
y.insert(2, 7)
print(y)

#인덱스가 아닌 값으로 지우기
y.remove(2)
print(y)

y.pop()
print(y)

ex = [88, 77]
#y.append(ex)    # 리스트 자체 삽입
y.extend(ex)    # 원소만 리스트에 삽입
print(y)

# 삭제: del, remove, pop

# 튜플 (순서O, 중복O, 수정X, 삭제X)
# 프로그램에 영향을 미치는,변경되지 않아야할 중요한 값을 저장
a = ()
b = (1,)
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', 'c'))

print(c[2])
print(c[3])
print(d[2][2])

print(d[2:])
print(d[2][0:2])

print(c + d)
print(c * 3)

# 튜플 함수
z = (5, 2, 1, 3, 4)
print(z)
print(3 in z)

# 값 3의 인덱스 반환
print(z.index(3))
# 값 1의 갯수 반환
print(z.count(1))
