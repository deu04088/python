f = open("sample.txt", "r")
lines = f.readlines()
sum = 0
for i in lines:
    sum += int(i)

print(sum/len(lines))

f.close()