# 151번
for num in [3, -20, -3, 44]:
    if num < 0:
        print(num)

# 152번
for num in [3, 100, 23, 44]:
    if num%3 == 0:
        print(num)

# 153번
for num in [13, 21, 12, 14, 30, 18]:
    if num < 20 and num%3 == 0:
        print(num)

# 154번
for lan in ["I", "study", "python", "language", "!"]:
    if len(lan) >= 3:
        print(lan)

# 155번
for lan in ["A", "b", "c", "D"]:
    if lan.isupper():
        print(lan)

# 156번
for lan in ["A", "b", "c", "D"]:
    if lan.islower():
        print(lan)

# 157번
for pet in ['dog', 'cat', 'parrot']:
    print(pet[0].upper(), pet[1:])

# 158번
for file in ['hello.py', 'ex01.py', 'intro.hwp']:
    a, b = file.split('.')
    print(a)
    
# 159번 160번
for file in ['intra.h', 'intra.c', 'define.h', 'run.py']:
    a = file.split('.')             #리스트로 분리되어 저장
    if (a[1] == 'h') or (a[1] == 'c'):
        print(file)

