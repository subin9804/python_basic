# Section04-4
# 파이썬 데이ㅣ터 타입(자료형)
# 딕셔너리, 집합 자료형

# 딕셔너리(Dictionary): 순서X, 중복X, 수정O, 삭제O

# Key, Value (Json과 유사)

# 선언
a = {'name' : 'kim', 'phone' : '010-7777-7777', 'birth': 980429}
b = {0: 'Hello Python', 1: 'Hello Coding'}
c = {'arr': [1, 2, 3, 4, 5]}

print(type(a))

# 출력
print(a['name'])
print(a.get('name'))
print(a.get('address')) # 키값이 존재하지 않아도 에러없음
print(c['arr'][1:3])

# 딕셔너리 추가
a['address'] = 'Seoul'
print(a)
a['rank'] = [1, 3, 4]
a['rank2'] = (1, 2, 3,)
print(a)

#keys, values, items
print(a.keys())
print(list(a.keys()))

temp = list(a.keys())
print(temp[1:3])

print(a.items())

print(a.values())
print(list(a.items()))

# 키값 존재유무
print(2 in b)
print('name' in a)
print('name2' not in a)

print()
print()

# 집합(Sets): 순서X, 중복X
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6, 6])

print(type(a))
print(c)

t = tuple(b)
print(t)
l = list(b)
print(l)

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합
print(s1.intersection(s2))
print(s1 & s2)

# 합집합
print(s1 | s2)
print(s1.union(s2))

# 차집합
print(s1 - s2)
print(s1.difference(s2))

# Sets 추가 / 제거
s3 = set([7, 8, 10, 15])

s3.add(18)
s3.add(7)

print(s3)

s3.remove(15)
print(s3)

print(type(s3))