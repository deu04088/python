# 291번                     잘 모르겠음
# f = open("C:/Users/deu04/OneDrive/Desktop/매수종목1.txt", "wt", encoding="utf-8")
# f.write("005930\n")
# f.write("005380\n")
# f.write("035420")
# f.close()

# 292번
# f = open("C:/Users/deu04/OneDrive/Desktop/매수종목2.txt", mode="wt", encoding="utf-8")
# f.write("005930 삼성전자\n")
# f.write("005380 현대차\n")
# f.write("035420 NAVER\n")
# f.close()

# 293번
# import csv

# f = open("C:/Users/deu04/OneDrive/Desktop/매수종목.csv", mode="wt", encoding="cp949", newline='')
# writer = csv.writer(f)
# writer.writerow(["종목명", "종목코드", "PER"])
# writer.writerow(["삼성전자", "005930", 15.59])
# writer.writerow(["NAVER", "035420", 55.82])
# f.close()

# 294번
f = open("C:/Users/deu04/OneDrive/Desktop/매수종목1.txt", "r", encoding="utf-8")

lines = f.readlines()
list = []

for i in lines:
    list.append(i)
    
print(list)

f.close()

# 295번
f = open("C:/Users/deu04/OneDrive/Desktop/매수종목2.txt", "r", encoding="utf-8")

lines = f.readlines()
dic = {}

for i in lines:
    key, value = i.split()
    dic[key] = value
    
print(dic)

f.close

# 296번
per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print(0)
    
# 297번
list = []

for i in per:
    try:
        a = float(i)
    except:
        a = 0
        
    list.append(a)
    
print(list)

# 298번
a = int(input("숫자를 입력하시오 : "))

try:
    a/0
except ZeroDivisionError:
    print("error")

# 299번             IndexError 찾아볼 것
data = [1, 2, 3]

for i in range(5):
    try:
        print(data[i])
    except IndexError as e:
        print(e)

# 300번             try 예외처리문 순서 숙지
for i in per:
    try:
        print(float(i))
    except:
        print(0)
    else:
        print("success")
    finally:
        print("All process clear")