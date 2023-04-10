# 231번
# def n_plus_1 (n) :
#     result = n + 1

# n_plus_1(3)
# print (result)
#결과 : result 호출 불가

# 232번
def make_url(chr):
    print("www.{}.com".format(chr))

make_url("naver")
print()

# 233번
def make_list(chr):
    print(list(chr))
make_list("abcd")
print()

# 234번
def pickup_even(li):
    a = []
    for i in li:
        if i%2 == 0:
            a.append(i)
    print(a)
pickup_even([3, 4, 5, 6, 7, 8])
print()

# 235번
def convert_int(chr):
    print(int(chr.replace(',', '')))

convert_int("1,234,567")

# 236번
def 함수(num) :
    return num + 4

a = 함수(10)
b = 함수(a)
c = 함수(b)
print(c)
#결과 : 22 출력

# 237번
def 함수(num) :
    return num + 4

c = 함수(함수(함수(10)))
print(c)
#결과 : 22 출력

# 238번
def 함수1(num) :
    return num + 4

def 함수2(num) :
    return num * 10

a = 함수1(10)
c = 함수2(a)
print(c)
#결과 : 140 출력

# 239번
def 함수1(num) :
    return num + 4

def 함수2(num) :
    num = num + 2
    return 함수1(num)

c = 함수2(10)
print(c)
#결과 : 16 출력

# 240번
def 함수0(num) :
    return num * 2

def 함수1(num) :
    return 함수0(num + 2)

def 함수2(num) :
    num = num + 10
    return 함수1(num)

c = 함수2(2)
print(c)
#결과 : 28 출력