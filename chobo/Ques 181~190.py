# 181번
apart = [['101호', '102호'], ['201호', '202호'], ['301호', '302호']]
print(apart)

# 182번
stock = [['시가', 100, 200, 300], ['종가', 80, 210, 330]]
print(stock)

# 183번
stock = {'시가' : [100, 200, 300], '종가' : [80, 210, 330]}
print(stock)

# 184번
stock = {'10/10' : [80, 110, 70, 90], '10/11' : [210, 230, 190, 200]}
print(stock)

# 185번
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in range(3):
    for j in range(2):
        print(apart[i][j], "호")
print()

# 186번
for i in range(3):
    for j in range(2):
        print(apart[2-i][j], "호")
print()
        
# 187번
for i in range(3):
    for j in range(2):
        print(apart[2-i][1-j], "호")
print()

# 188번
for i in range(3):
    for j in range(2):
        print(apart[i][j], "호")
        print('-----')
print()

# 189번
for i in range(3):
    for j in range(2):
        print(apart[i][j], "호")
    print('-----')
print()

# 190번
for i in range(3):
    for j in range(2):
        print(apart[i][j], "호")
print('-----')

