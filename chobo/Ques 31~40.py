#31번
a = "3"
b = "4"
print(a+b)              #문자로 인식

#32번
print("Hi" * 3)

#33번
print("-" * 80)

#34번
t1 = 'python'
t2 = 'java'
t3 = t1 + ' ' + t2 + ' '
print(t3 * 5)

#35번
name1 = '김민수'
age1 = 10
name2 = '이철희'
age2 = 13

print("이름 : %s 나이 : %d" %(name1, age1))
print("이름 : %s 나이 : %d" %(name2,age2))          #C문법이랑 헷갈리지 말 것

#36번
print("이름 : {} 나이 : {}".format(name1, age1))
print("이름 : {} 나이 : {}".format(name2,age2))          #문법 다시 공부

#37번
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")                #처음 봄

#38번
mon = "5,969,782,550"
tmp1 = mon.replace(",", "")
tmp2 = int(tmp1)
print("%d" %tmp2)

#39번
section = "2020/03(E) (IFRS연결)"
print(section[:7])

#40번
data = "   삼성전자    "
tmp3 = data.strip()
print(tmp3)

