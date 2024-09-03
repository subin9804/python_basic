# Section07-1
# 파이썬 클래스 상세 이해
# Self, 클래스, 인스턴스 변수

# 네임스페이스: 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수: 직접 사용 가능, 객체보다 먼저 생성
# 인스턴스 변수: 객체마다 별도로 존재, 인스턴스 생성 후 사용

# 선언
# class 클래스명:
#     함수
#     함수
#     함수


# 예제1
class UserInfo:
    # 속성, 메소드
    # __init__ 클래스 초기화 메서드
    def __init__(self, name):
        self.name = name

    def user_info_p(self):
        print("Name: ", self.name)

# 네임스페이스: 인스턴스가 갖고 있는 각각의 저장 공간
user1 = UserInfo("Kim")
user1.user_info_p()
user2 = UserInfo("Park")
user2.user_info_p()

# id(): 메모리의 주소값
print(id(user1))
print(id(user2))
# __dict__: 네임스페이스
print(user1.__dict__)
print(user2.__dict__)


# 예제2
# self의 이해
class SelfTest:
    def function1():
        print('function1 called!')

    def function2(self):
        print(id(self))
        print('function2 called!')

self_test = SelfTest()

# 함수에 self 인자가 없을 경우 클래스에서 직접 호출해야 한다. : 공통함수
#self_test.function1()
SelfTest.function1()

self_test.function2()
print(id(self_test))

# 클래스로 self 인자를 가진 함수를 호출하려면?
SelfTest.function2(self_test)


# 예제3
# 클래스 변수, 인슽턴스 변수
class WareHouse:
    # 클래스 변수
    stock_num = 0
    def __init__(self, name):
        self.name = name
        WareHouse.stock_num += 1
    def __del__(self):
        WareHouse.stock_num -= 1

user1 = WareHouse('Kim')
user2 = WareHouse('Park')
user3 = WareHouse('Lee')

# 클래스 내부에서 선언한 stock_num은 나오지 않는다.
print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)

# 클래스 네임스페이스, 클래스 변수(공유)
print(WareHouse.__dict__)

# 자기 네임스페이스에 없으면 클래스 네임스페이스에서 찾음
print(user1.stock_num)
print(user2.stock_num)
print(user3.stock_num)

# __del__ 메서드와 연결
del user1

print(user2.stock_num)
print(user3.stock_num)