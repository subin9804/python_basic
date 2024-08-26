# Section05-3
# 조건문, 반복문 중간 점검 퀴즈

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 = {"봄": "딸기", "여름": "토마토", "가을":"사과"}
for i in q1.keys():
    if i == "가을":
        print(q1[i])


# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 = {"봄": "딸기", "여름": "토마토", "가을":"사과"}
for k,v in q2.items() :
    if v == "사과":
        print("사과 찾음")  
        break
else:
    print('사과 못찾음ㅠㅠ')


# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 : B학점
# 41 ~ 60 : C학점
# 21 ~ 40 : D학점
# 0 ~ 20 : E학점

score = 33
result = ""
if score > 80 :
    result = 'A학점'
elif score > 60 :
    result = 'B학점'
elif score > 40 :
    result = 'C학점'
elif score > 20 :
    result = 'D학점'
elif score >= 0 :
    result = 'E학점'

print(result)

# 4. 다음 세 개의 숫자 중 가장 큰 수를 출력하세요.(if문 사용)
a, b, c = 12, 6, 18

best = a
for i in list([a, b, c]):
    if best < i :
        best = i

print("best: ", best)

# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1, 3: 남자, 2, 4: 여자)
q5 = '000000-2000000'
#if q5[7] == (1 or 3):
if int(q5[7]) % 2 == 1:
    print('남자')
else:
    print('여자')

# 6 ~ 10 반복문 사용
# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q6 = ["갑", "을", "병", "정"]
for i in q6:
    if i == "정":
        continue
    else: 
        print(i)

# list comprehension example
q66 = [x for x in q6 if x != '정']
print(q66)

# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.
for i in range(101):
    if(i % 2 == 1):
        print(i, end=",")
    
print()
# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q8 = ["nice", "study", "python", "anaconda", "!"]
for i in q8:
    if len(i) >= 5:
        print(i, end=" ")

print()
# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q9 = ["A", "b", "c", "D", "e", "F", "G", "h"]
for i in q9:
    if i.islower():
        print(i, end="")

print()
# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q10 = ["A", "b", "c", "D", "e", "F", "G", "h"]
for i in q10:
    if i.islower() :
        print(i.upper(), end="")
    else:
        print(i.lower(), end="")

# 리스트 컴프리헨션
numbers = []

for n in range(1, 101):
    numbers.append(n)
print(numbers)

# x에 1부터 101까지 할당
numbers2 = [x for x in range(1, 101)]
print(numbers2)