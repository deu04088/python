# 191번
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
for i in range(3):
    for j in range(4):
        print(data[i][j] + data[i][j]*0.00014)

# 192번
for i in range(3):
    for j in range(4):
        print(data[i][j] + data[i][j]*0.00014)
    print('----')

# 193번
result = []
for i in range(3):
    for j in range(4):
        result.append(data[i][j] + data[i][j]*0.00014)
print(result)

# 194번
result = []
for i in range(3):
    tmp = []
    for j in range(4):
        tmp.append(data[i][j] + data[i][j]*0.00014)
    result.append(tmp)
print(result)

# 195번
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for i in range(1,4):
    print(ohlc[i][3])
print()

# 196번
for i in range(1,4):
    if ohlc[i][3] > 150:
        print(ohlc[i][3])
print()

# 197번
for i in range(1,4):
    if ohlc[i][3] >= ohlc[i][0]:
        print(ohlc[i][3])
print()

# 198번
volatility = []
for i in range(1,4):
    volatility.append(ohlc[i][1] - ohlc[i][2])
print(volatility)
print()

# 199번
volatility = []
for i in range(1,4):
    if ohlc[i][3] > ohlc[i][0]:
        volatility.append(ohlc[i][1] - ohlc[i][2])
print(volatility)
print()

# 200번
sum = 0
for i in range(1,4):
    sum += (ohlc[i][3] - ohlc[i][0])
print(sum)
        