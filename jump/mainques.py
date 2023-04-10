# 1. 문자열 바꾸기
a = "a:b:c:d"
a = a.split(':')
print(a)
a = "#".join(a)
print(a)

# 2.딕셔너리 값 추출하기
a = {'A' : 90, 'B' : 80}
print(a.get('C', 70))

# 3.리스트의 더하기와 extend 함수
a = [1,2,3]
a = a + [4,5]
print(a)

a = [1,2,3]
a.extend([4,5])
print(a)

# 4.리스트 총합 구하기
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
sum = 0
for i in A:
    if i >= 50:
        sum += i
print(sum)

# 5.피보나치 수열
def fibo(i):
    if i == 1:
        return 0
    elif i == 2:
        return 1
    else:
        return fibo(i-1) + fibo(i-2) 
print(fibo(5))

# # 6.숫자의 총합 구하기
# a = input("숫자 입력 :")
# a = a.split(',')
# sum = 0
# for i in a:
#     sum += int(i)
# print(sum)

# # 7.한 줄 구구단
# gugu = int(input("구구단을 출력할 숫자를 입력하세요(2~9):"))
# print(1*gugu, 2*gugu, 3*gugu, 4*gugu, 5*gugu, 6*gugu, 7*gugu, 8*gugu, 9*gugu)
# print()

# 8.역순 저장
f = open("D:/python/jump/abc.txt", 'r')
line = f.readlines()
line = line[::-1]
for li in line:
    li = li.strip()
    print(li)
f.close

# 9.평균값 구하기
