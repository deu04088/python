# 211번
def 함수(문자열) :
    print(문자열)

함수("안녕")
함수("Hi")
#결과 : 안녕 HI
print()

# 212번
def 함수(a, b) :
    print(a + b)

함수(3, 4)
함수(7, 8)
#결과 : 7 15
print()

# 213번
# def 함수(문자열) :
#     print(문자열)
# 함수()
# 정해진 형식대로 매개변수를 넣지 않고 호출했기 때문에

# 214번
# def 함수(a, b) :
#     print(a + b)

# 함수("안녕", 3)
# 정해진 형식의 매개변수가 들어가지 않았기 때문에

# 215번
def print_with_smile(str):
    print(str, ":D")
   
    
# 216번
print_with_smile('안녕하세요') 
print()

# 217번
def print_upper_price(price):
    print(price*1.3)
    
print_upper_price(100)
print()

# 218번
def print_sum(a, b):
    print(a + b)

# 219번
def  print_arithmetic_operation(a, b):
    print('{} + {} = {}'.format(a, b, a+b))
    print('{} - {} = {}'.format(a, b, a-b))
    print('{} * {} = {}'.format(a, b, a*b))
    print('{} / {} = {}'.format(a, b, a/b))
    
print_arithmetic_operation(3, 4)

# 220번
def print_max(a, b, c):
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    else:
        print(c)
        
print_max(1, 2, 3) 
