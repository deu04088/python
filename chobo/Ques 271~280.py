# 271번
import random
class Account():
    def __init__(self, user, price):
        self.user = user
        self.price = price
    
        self.bank = 'SC은행'
        
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)
        
        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        
        self.account = num1 + '-' + num2 + '-' + num3
         
kim = Account("김민수", 100)
print(kim.user)
print(kim.price)
print(kim.bank)
print(kim.account)

# 272번
class Account():
    cnt = 0
    
    def __init__(self, user, price):
        self.user = user
        self.price = price
    
        self.bank = 'SC은행'
        
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)
        
        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        
        self.account = num1 + '-' + num2 + '-' + num3
        Account.cnt += 1
        
kim = Account("김민수", 100)
print(Account.cnt)
park = Account("박주영", 200)
print(Account.cnt)

# 273번             왜 self가 아닌 변수를 넣어야 하는가???
class Account():
    cnt = 0
    
    def __init__(self, user, price):
        self.user = user
        self.price = price
    
        self.bank = 'SC은행'
        
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)
        
        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        
        self.account = num1 + '-' + num2 + '-' + num3
        Account.cnt += 1
        
    def get_account_num(a):
        print(a.cnt)
        
kim = Account("김민수", 100)
park = Account("박주영", 200)
kim.get_account_num
park.get_account_num

# 274번
class Account():
    cnt = 0
    
    def __init__(self, user, price):
        self.user = user
        self.price = price
    
        self.bank = 'SC은행'
        
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)
        
        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        
        self.account = num1 + '-' + num2 + '-' + num3
        Account.cnt += 1
        
    def get_account_num(a):
        print(a.cnt)
        
    def deposit(self, amount):
        if amount >= 1:
            self.price += amount

kim = Account("김민수", 100)
kim.deposit(200)
print(kim.price)

# 275번
class Account():
    cnt = 0
    
    def __init__(self, user, price):
        self.user = user
        self.price = price
    
        self.bank = 'SC은행'
        
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)
        
        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        
        self.account = num1 + '-' + num2 + '-' + num3
        Account.cnt += 1
        
    def deposit(self, amount):
        if amount >= 1:
            self.price += amount
            
    def withdraw(self, money):
        if money <= self.price:
            print(money, "원을 출금하였습니다.")
            self.price -= money
            
kim = Account("김민수", 500)
kim.withdraw(200)
print(kim.price)

# 276번
class Account():
    cnt = 0
    
    def __init__(self, user, price):
        self.user = user
        self.price = price
    
        self.bank = 'SC은행'
        
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)
        
        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        
        self.account = num1 + '-' + num2 + '-' + num3
        Account.cnt += 1
        
    def deposit(self, amount):
        if amount >= 1:
            self.price += amount
            
    def withdraw(self, money):
        if money <= self.price:
            print(money, "원을 출금하였습니다.")
            self.price -= money
            
    def display_info(self):
        print("은행이름 :", self.bank)
        print("예금주 :", self.user)
        print("계좌번호 :", self.account)
        print("잔고 :", self.price)
        
kim = Account("김민수", 10000)
kim.display_info()
        

# 277번
class Account():
    cnt = 0
    
    def __init__(self, user, price):
        self.user = user
        self.price = price
    
        self.bank = 'SC은행'
        self.plus = 0
        
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)
        
        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        
        self.account = num1 + '-' + num2 + '-' + num3
        Account.cnt += 1
        
    def deposit(self, amount):
        if amount >= 1:
            self.price += amount
            
    def withdraw(self, money):
        if money <= self.price:
            print(money, "원을 출금하였습니다.")
            self.price -= money
            self.plus += 1
            
        if self.plus%5 == 0:
            self.price = self.price + self.price*0.01
            print(self.price)
            
    def display_info(self):
        print("은행이름 :", self.bank)
        print("예금주 :", self.user)
        print("계좌번호 :", self.account)
        print("잔고 :", self.price)
        
kim = Account("김민수", 10000)
kim.withdraw(100)
kim.withdraw(100)
kim.withdraw(100)
kim.withdraw(100)
kim.withdraw(100)

# 278번                     결과 이상함
        
kim = Account("김민수", 10000)
lee = Account("이민수", 20000)
park = Account("박준", 30000)

list = []
list.append(kim)
list.append(lee)
list.append(park)

print(list)

# 279번             
ryu = Account("류", 10000000)
list.append(ryu)

for i in list:
    if i.price>=1000000:
        print(i.display_info())
        
# 280번 
class Account():
    cnt = 0
    
    def __init__(self, user, price):
        self.user = user
        self.price = price
    
        self.bank = 'SC은행'
        self.plus = 0
        self.w_recode = []
        self.d_recode = []
        
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)
        
        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        
        self.account = num1 + '-' + num2 + '-' + num3
        Account.cnt += 1
        
    def deposit(self, amount):
        if amount >= 1:
            self.price += amount
            self.d_recode.append(amount)
            
    def withdraw(self, money):
        if money <= self.price:
            print(money, "원을 출금하였습니다.")
            self.price -= money
            self.plus += 1
            self.w_recode.append(money)
            
        if self.plus%5 == 0:
            self.price = self.price + self.price*0.01
            print(self.price)
            
    def display_info(self):
        print("은행이름 :", self.bank)
        print("예금주 :", self.user)
        print("계좌번호 :", self.account)
        print("잔고 :", self.price)
        
    def deposit_history(self):
        for i in self.d_recode:
            print(i, "원을 입금했습니다")
        
    def withdraw_history(self):
        for i in self.w_recode:
            print(i, "원을 인출했습니다.")
            
kim = Account("김민수", 10000)
kim.deposit(500)
kim.deposit(200)

kim.withdraw(600)
kim.withdraw(300)

kim.deposit_history()
kim.withdraw_history()
