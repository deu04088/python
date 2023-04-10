# 251번
# 252번
class Human:
    pass

# 253번
areum = Human()

# 254번
class Human():
    def __init__(self):
        print("응애응애")

areum = Human()
print()

# 255번
class Human():
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
areum = Human("아름", 25, "여자")        
print(areum.name)

# 256번
print(areum.name, areum.age, areum.sex)

# 257번
class Human():
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    def who(self):
        print("이름: {} 나이: {} 성별: {}".format(self.name, self.age, self.sex))
        
areum = Human("아름", 25, "여자")        
areum.who()
print("-"*40)

# 258번
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def who(self):
        print("이름: {} 나이: {} 성별: {}".format(self.name, self.age, self.sex))

    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


areum = Human("불명", "미상", "모름")
areum.who()      # Human.who(areum)

areum.setInfo("아름", 25, "여자")
areum.who()      # Human.who(areum)

# 259번
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __del__(self):
        print("나의 죽음을 알리지마라")

    def who(self):
        print("이름: {} 나이: {} 성별: {}".format(self.name, self.age, self.sex))

    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

areum = Human("아름", 25, "여자")
del(areum)

# 260번
class OMG : 
    def prin(self) :        #self를 넣어서 문제 해결
        print("Oh my god")
        
a = OMG()
a.prin()           #파이썬 인터프리터가 자동으로 메소드를 호출할 때 인자를 넣어버림
