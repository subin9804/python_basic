# Section07-2
# 파이썬 클래스 상세 이해
# 상속, 다중상속

# 예제1
# 상속 기본
# 슈퍼클래스(부모) 및 서브클래스(자식) -> 모든 속성, 메소드 사용 가능

# 라면 -> 속성(종류, 회사, 맛, 면종류, 이름) : 부모(공통적인 속성)

class Car:
    """Parent Class"""
    def __init__(self, type, color):
        self.type = type
        self.color = color

    def show(self):
        return 'Car Class "Show Method!"'

# 클래스를 파라미터로 넣어주면 해당 클래스의 속성을 사용할 수 있다.
class BMWCar(Car):
    """Sub Class"""
    def __init__(self, car_name, type, color):
        super().__init__(type, color)
        self.car_name = car_name
    
    def show_model(self) -> None:
        return "Your Car Name: %s" % self.car_name

class BenzCar(Car):
    """Sub Class"""
    def __init__(self, car_name, type, color):
        super().__init__(type, color)
        self.car_name = car_name
    
    def show_model(self) -> None:
        return "Your Car Name: %s" % self.car_name

    def show(self):
        print(super().show())
        return 'Car Info : %s %s %s' %(self.car_name, self.color, self.type)

model1 = BMWCar("520d", "sedan", "red")
print(model1.color) # Super
print(model1.type) # Super
print(model1.car_name) # Sub
print(model1.show()) # Super
print(model1.show_model()) # Sub
print(model1.__dict__)

# Method Overriding (오버라이딩)
# 부모 클래스의 메서드를 재구현할 수 있다.
model2 = BenzCar("220d", "sub", "black")
print(model2.show())

# Parent Method Call
model3 = BenzCar("350s", "sedan", "silver")
print(model3.show())

# Inheritance Info (상속 정보)
print(BMWCar.mro())
print(BenzCar.mro())

# 예제2
# 다중 상속
class X():
    pass

class Y():
    pass

class Z():
    pass

class A(X, Y):
    pass

class B(Y, Z):
    pass

class M(B, A, Z):
    pass

print(M.mro())