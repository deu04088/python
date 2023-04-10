# 102번
print(3 == 5)
#>>> False

# 103번
print(3 < 5)
#>>> True

# 104번
x = 4
print(1 < x < 5)
#>>> True

# 105번
print((3 == 3) and (4 != 3))
#>>> True

# 106번
# print(3 => 4)   //   잘못된 연산
print(3 >= 4) 
#>>> False

# 107번
if 4 < 3:
    print("Hello world")
# 실행 안됨

# 108번
if 4 < 3:
    print("Hello world")
else:
    print("Hi, there")
#>>> Hi, there

# 109번
if True:
    print("1")
    print("2")
else:
    print("3")
print("4")
#>>> 124

# 110번
if True:
    if False:
        print("1")
        print("2")
    else:
        print("3")
else:
    print("4")
print("5")
#>>> 35