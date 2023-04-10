# 161번
for i in range(100):
    print(i)
    
# 162번
for year in range(2002, 2051, 4):
    print(year)

# 163번
for i in range(3, 31, 3):
    print(i)

# 164번
for i in range(99, -1, -1):
    print(i)

# 165번
for f in range(10):
    print(f/10)

# 166번
for mul in range(10):
    print("3X{} = {}".format(mul, mul*3))

# 167번
for mul in range(10):
    if mul%2 == 1:
        print("3X{} = {}".format(mul, mul*3))

# 168번
sum = 0
for i in range(11):
    sum += i
print(sum)

# 169번
sum = 0
for i in range(11):
    if(i%2 == 1):
        sum += i
print(sum)

# 170번
mul = 1
for i in range(1,11):
    mul *= i
print(mul)
