# 281번
class Car():
    def __init__(self, wheel, price):
        self.wheel = wheel
        self.price = price

car = Car(2, 1000)
print(car.wheel)
print(car.price)

# 282번
class Bike(Car):
    pass
    
# 283번
bike = Bike(4, 10000)
print(bike.wheel)
print(bike.price)

# 284번                 상속을 받아도 다시 초기화해야 함
class Bike(Car):
    def __init__(self, wheel, price, system):
        super().__init__(wheel, price)
        self.system = system
        
bike = Bike(2, 100, "시마노")
print(bike.wheel)
print(bike.price)
print(bike.system)
print()

# 285번
class Sedan(Car):
    def __init__(self, wheel, price):
        super().__init__(wheel, price)
        
    def info(self):
        print(self.wheel)
        print(self.price)

car = Sedan(4, 1000)
car.info()
print()

# 286번
class Bike(Car):
    def __init__(self, wheel, price, system):
        super().__init__(wheel, price)
        self.system = system
        
    def info(self):
        print(self.wheel)
        print(self.price)
        print(self.system)

bicycle = Bike(2, 100, "시마노")
bicycle.info()
print()

# 287번
# 286번에서 같이 함

# 288번
class 부모:
  def 호출(self):
    print("부모호출")

class 자식(부모):
  def 호출(self):
    print("자식호출")
    
나 = 자식()
나.호출()
# 결론 : 메소드 오버라이딩 발생
print()

# 289번
class 부모:
  def __init__(self):
    print("부모생성")

class 자식(부모):
  def __init__(self):
    print("자식생성")
    
나 = 자식()
# 결론 : super()로 초기값 상속이 되지 않음
print()

# 290번
class 부모:
  def __init__(self):
    print("부모생성")

class 자식(부모):
  def __init__(self):
    print("자식생성")
    super().__init__()

나 = 자식()
# 결론 : super()로 초기값을 상속으로 가져옴