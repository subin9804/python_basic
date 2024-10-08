# Section02-2
# 파이썬 기초 코딩
# 몸풀기 코딩 실습

# import this
import sys

# 파이썬 기본 인코딩
print(sys.stdin.encoding)
print(sys.stdout.encoding) 

# 출력문
print('My name is GoodGirl!')

# 변수 선언 (값을 할당)
myName = 'GoodBoy'

# 조건문
if myName == 'GoodBoy':
    print('Ok')
elif myName == 'BadBoy':
    print('No')

# 반복문
for i in range(1, 10):
    for j in range(1, 10):
        #print('{0:d} * {1:d} = ' .format(i,j), i*j)
        print('%d * %d = ' % (i, j), i*j)
# 변수 선언 (한글)
이름 = '좋은사람'

# 출력(한글)
print(이름)

# 함수 선언
def 인사():
    print("안녕하세요. 반갑습니다.")

인사()

def greeting():
    print('Hello!')

greeting()

# 클래스
class Cookie:
    pass

# 객체 생성(인스턴스)
cookie = Cookie()

# 객체에 대한 정보
print(id(cookie))
print(dir(cookie))
