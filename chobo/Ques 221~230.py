# 221번
def print_reverse(str):
    print(str[::-1])            #reverse 함수는 쓸 수 없는지??

print_reverse("python")

# 222번
def print_score(score):
    print(sum(score)/len(score))
print_score ([1, 2, 3])
print()

# 223번
def print_even(even):
    for i in range(len(even)):
        if even[i]%2 == 0:
            print(even[i])
            
print_even ([1, 3, 2, 10, 12, 11, 15])
print()

# 224번
def print_keys(dic_key):
    print(dic_key.keys())

print_keys ({"이름":"김말똥", "나이":30, "성별":0})
print()

# 225번
my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}

def print_value_by_key(dic, day):
    print(dic[day])
    
print_value_by_key (my_dict, "10/26")

# 226번             #고민해봐야 했던 문제
def print_5xn(chr):
    for i in range(int(len(chr)/5)):
        print(chr[5*i:5*i+5])
    
print_5xn("아이엠어보이유알어걸")
print()

# 227번
def printmxn(chr, num):
    for i in range(int(len(chr)/num+1)):
        print(chr[num*i:num*i+num])
    
printmxn("아이엠어보이유알어걸", 3)
print()

# 228번
def calc_monthly_salary(annual_salary):
    print(int(annual_salary/12))
    
calc_monthly_salary(12000000)
print()

# 229번
def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(a=100, b=200)
#결과 : 왼쪽 : 100 오른쪽 : 200

# 230번
def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(b=100, a=200)
#결과 : 왼쪽 : 200 오른쪽 : 100
