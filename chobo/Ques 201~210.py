# 201번
def print_coin():
    print("비트코인")
print()

# 202번
print_coin()

# 203번
for i in range(100):
    print_coin()
print()

# 204번
def print_coins():
    for i in range(100):
        print_coin()

# 205번
# hello()
# def hello():
#     print("Hi")
#함수 정의 전에 사용되어서

# 206번
def message() :
    print("A")
    print("B")

message()
print("C")
message()
#결과 : ABCAB
print()

# 207번
print("A")

def message() :
    print("B")

print("C")
message()
#결과 : ACB
print()

# 208번
print("A")
def message1() :
    print("B")
print("C")
def message2() :
    print("D")
message1()
print("E")
message2()
#결과 : ACBED
print()

# 209번
def message1():
    print("A")

def message2():
    print("B")
    message1()

message2()
#결과 : BA
print()

# 210번
def message1():
    print("A")

def message2():
    print("B")

def message3():
    for i in range (3) :
        message2()
        print("C")
    message1()

message3()
#결과 : BCBCBCA