# 171번
price_list = [32100, 32150, 32000, 32500]
for i in range(4):
    print(price_list[i])

# 172번
for i in range(4):
    print(i, price_list[i])

# 173번
for i in range(4):
    print(3-i, price_list[i])

# 174번
for i in range(1, 4):
    print(10*i+100, price_list[i])

# 175번
my_list = ["가", "나", "다", "라", "마"]
for i in range(3):
    print(my_list[i], my_list[i+1])

# 176번
for i in range(3):
    print(my_list[i], my_list[i+1], my_list[i+2])

# 177번
my_list1 = ["가", "나", "다", "라"]
for i in range(3, 0, -1):
    print(my_list1[i], my_list1[i-1])
    
# 178번
my_list2 = [100, 200, 400, 800]
for i in range(3):
    print(my_list2[i+1]-my_list2[i])

# 179번
my_list3 = [100, 200, 400, 800, 1000, 1300]
for i in range(4):
    print((my_list3[i]+my_list3[i+1]+my_list3[i+2])/3)

# 180번
volatility = []
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
for i in range(5):
    volatility.append(high_prices[i] - low_prices[i])
print(volatility)