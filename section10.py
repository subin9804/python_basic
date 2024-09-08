# Section10
# 파이썬 예외처리의 이해

# 예외 종류
# 문법적으로 에러가 없지만, 코드 실행(런타임)프로세스에서 발생하는 예외 처리도 중요
# linter: 코드 스타일, 문법 체크


# SyntaxError: 잘못된 문법
#   print('Test')
#   if True
#       pass
#   x => y :

# NameError: 참조변수 없음
#   a = 10
#   b = 15
#   print(c)

# ZeroDivisionError: 0나누기 에러
# print(10 / 0)

# IndexError: 인덱스 범위 오버
#   x = [10, 20, 30]
#   print(x[3]) : 예외발생

# KeyError: 존재하지 않는 키를 호출할 때
# get 메소드를 이용하면 none을 반환하며 에러 발생X
#   dic = {'name': 'Kim', 'Age': 33, 'City': 'Seoul'}
#   print(dic['hobby'])
#   print(dic.get('hobby'))

# AttributeError: 모듈, 클래스에 있는 잘못된 속성 사용시에 예외
import time
print(time.time())
#print(time.month())

# ValueError: 참조값이 없을 때 발생
#   x = [1, 5, 9]
#   x.remove(9)
#   x.index(9)

# fileNotFoundError: 파일이 해당 경로에 존재하지 않을때 발생
#   f = open('test.txt', 'r')

# TypeError
a = [1, 2]
b = (1, 2)
c = 'test'

#   print(a + b)
#   print(a + c)
print(a + list(b)) # 형변환

# 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩
# 그후 런타임 예외 발생ㅇ시 예외 처리 코딩 권장(EAFP 코딩 스타일)

# 예외 처리 기본
# try: 에러가 발생한 가능성이 있는 코드 실행
# except: 에러명1
# except: 에러명2
# else: 에러가 발생하지 않았을 경우 실행
# finally: 항상 실행

# 예제1
name = ['Kim', 'Lee', 'Park']
try:
    z = 'Kim'
    x = name.index(z)
    print('{} found it! in name'.format(z, x+1))
except ValueError:
    print('Not found it! = Occurred ValueError!')
else:
    print('Ok! else!')


try:
    z = 'Kim'
    x = name.index(z)
    print('{} found it! in name'.format(z, x+1))
except :    # 특정 에러를 지정하지 않으면 모든 에러 캐치
    print('Not found it! = Occurred Error!')
else:
    print('Ok! else!')

# 예제 3
try:
    z = 'Kim'
    x = name.index(z)
    print('{} found it! in name'.format(z, x+1))
except :
    print('Not found it! = Occurred Error!')
else:
    print('Ok! else!')
finally:    # 예외 발생 유무에 관계없이 실행
    print('finally ok!')


# 예제 4
# 예외 처리는 하지 않지만, 무조건 수행되는 코딩 패턴

try:
    print('try')
finally:
    print('Ok finally!!!')

# 예외5
try:
    z = 'Kim'
    x = name.index(z)
    print('{} found it! in name'.format(z, x+1))
except ValueError as l: # 별칭을 지정해서 에러내용 프린트
    print('Not found it! = Occurred ValueError!')
    print(l)
except IndexError:
    print('Not found it! = Occurred IndexError!')
except Exception:
    print('Not found it! = Occurred Error!')
else:
    print('Ok! else!')
finally:  
    print('finally ok!')

# 예제6
# 예외 발생: raise
# raise 키워드로 예외 직접 발생
try:
    a = 'Kim'
    if a == 'Kim':
        print('허가!')
    else:
        raise ValueError
except ValueError:
    print('문제 발생')
except Exception as f:
    print(f)
else:
    print('Ok!')