# 141번
for lis in [100, 200, 300]:
    print(lis + 10)
    
# 142번
for menu in ["김밥", "라면", "튀김"]:
    print("오늘의 메뉴 :", menu)

# 143번
for cop in ["SK하이닉스", "삼성전자", "LG전자"]:
    print(len(cop))

# 144번
for pet in ['dog', 'cat', 'parrot']:
    print(pet, len(pet))

# 145번
for pet in ['dog', 'cat', 'parrot']:
    print(pet[0])

# 146번
for mul in [1, 2, 3]:
    print("3 X", mul)

# 147번
for mul in [1, 2, 3]:
    print("3 X {} = {}".format(mul, mul*3))

# 148번                 ???? 이게 맞나 싶음..
리스트 = ["가", "나", "다", "라"]
for kor in 리스트[1:]:
    print(kor)

# 149번
for kor in 리스트[::2]:
    print(kor)

# 150번
for kor in 리스트[::-1]:
    print(kor)
