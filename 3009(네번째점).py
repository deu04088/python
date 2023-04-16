x = []
y = []
for i in range(3):
    A, B = map(int, input().split())
    x.append(A)
    y.append(B)
    
for i in range(3):
    if x.count(x[i]) == 1:
        anw_x = x[i]
    if y.count(y[i]) == 1:
        anw_y = y[i]
        
print(anw_x, anw_y)