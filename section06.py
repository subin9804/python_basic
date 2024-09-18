# Section06
# 파이썬 함수식 및 람다(lambda)

# 함수 정의 방법
# def 함수명(parameter):
#   code

# 함수 호출
# 함수명(parameter)

# 함수 선언 위치 중요

# 예제1
def hello(world):
    print("Hello", world)

hello("Python!")
hello(7777)

# 예제2
def hello_return(world):
    val = "Hello" + str(world)
    return val

str = hello_return("Python!!!!!")
print(str)

# 예제3 (다중리턴)
# 리턴되는 값의 개수만큼 받을 수 있는 변수 필요
def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3

val1, val2, val3 = func_mul(100)
print(val1, val2, val3)


# 예제4 (데이터 타입 반환)
# 효율적인 데이터 재구성 가능
def func_mul2(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]

lt = func_mul2(100)
print(lt, type(lt))

# 예제4
# *args, *kwargs
# 가변 파라미터 - 튜플형태의 파라미터로 변환
def args_func(*args):
    #for t in args:
    #    print(t)

    # index 생성
    for i,v in enumerate(args):
        print(i, v)

args_func('kim')
args_func('kim', 'Park')
args_func('kim', 'Park', 'Lee')


# kwargs
# **는 딕셔너리 형태의 파라미터 가능
def kwargs_func(**kwargs):
    for k, v in kwargs.items() :
        print(k, v)

kwargs_func(name1='kim', name2="Park", name3='Lee')


# 전체 혼합
def example_mul(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)

example_mul(10, 20)
example_mul(10, 20, 'park', 'kim', 'Lee', age=1, age2=33, age3=55)

 
# 중첩함수(클로저)
# 변수 선언 최소화
# 메모리 관리 효율
def nested_func(num):
    def func_in_func(num):
        print(num)
    print("in func")
    func_in_func(num + 10000)

nested_func(10000)

# 예제6(hint)
def func_mul3(x : int) -> list:
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]

print(func_mul3(5.0))

# 람다식 예제
# 람다식: 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행(Heap 초기화) -> 메모리 초기화

# 일반적 함수 -> 변수 할당
def mul_10(num : int) -> int:
    return num * 10

var_func = mul_10
print(var_func)
# function이라는 클래스로 메모리 점유
print(type(var_func))

lambda_mul = lambda num: num * 10
print('>>>', lambda_mul(10))


def func_final(x, y, func):
    print(x * y * func(10))

func_final(10, 10, lambda_mul)

print(func_final(10, 10, lambda x : x * 1000))

