# 121번
alpha = input()
if alpha.islower():
    print(alpha.upper())
else:
    print(alpha.lower())            #islower, isupper 알아둘 것
    
# 122번
score = int(input())
if 80 < score and score <=100:
    print("grade is A")
elif 60 < score <= 80:
    print("grade is B")
elif 40 < score <= 60:
    print("grade is C")
elif 20 < score <= 40:
    print("grade is D")
else:
    print("grade is F")
    
# 123번         (어려움)
money = {'달러' : 1167, '엔' : 1.096, '유로' : 1268, '위안' : 171}
num, currency = input("입력 : ").split()        # 금액과 환율 단위 분리 
print(num, currency)
print(float(num)*money[currency])       #금액은 실수화하고 money 딕셔너리의 key와 currency가 일치하는 value를 반환 

# 124번
num1 = int(input("number1 : "))
num2 = int(input("number2 : "))
num3 = int(input("number3 : "))

if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 > num3:
    print(num2)
else:
    print(num3)

# 125번
com = {'011' : 'SKT', '016' : 'KT', '019' : 'LGU', '010' : '알수없음'}
phone = input("휴대전화 번호 입력 : ")
ph1, ph2, ph3 = phone.split('-')
print("당신은 {0} 사용자입니다.".format(com[ph1]))

# 126번
post = input("우편번호 : ")
tmp = post[:3]
if tmp in ['010', '011', '012']:
    print("강북구")
elif tmp in ['013', '014', '015']:
    print('도봉구')
else:
    print('노원구')

# 127번             논의!!!!!!
res = input("주민등록번호 : ")
fron, back = res.split("-")
print(fron, back)
print(back[0])
if back[0] == 1:                #?????????
    print("남자")
else:
    print("여자")

# 128번             위 문제와의 차이
if back[1:3] in ['00', '01', '02', '03', '04', '05', '06', '07', '08']:
    print("서울 입니다.")
elif back[1:3] in ['09', '10', '11', '12']:
    print("부산입니다")
else:
    print("그 외 타 지역입니다")
    
# 129번
sum = int(fron[0])*2 + int(fron[1])*3 + int(fron[2])*4 + int(fron[3])*5 + int(fron[4])*6 + \
    int(fron[5])*7 + int(back[0])*8 + int(back[1])*9 + int(back[2])*2 + int(back[3])*3 + int(back[4])*4 + int(back[5])*5 
sum2 = int(11 - (sum%11))
if back[6] == sum2:
    print("유효한 주민등록번호입니다")
else:
    print("유효하지 않은 주민등록번호입니다.")

# 130번
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
change = float(btc['max_price']) - float(btc['min_price'])
price = float(btc['opening_price'])
max = float(btc['max_price'])

if (price+change) > max:
    print("상승장")
else:
    print("하락장")