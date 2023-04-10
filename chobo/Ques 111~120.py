# 111번
print("안녕하세요"*2)

# 112번
a = input("숫자를 입력하세요 : ")
print(int(a) + 10)

# 113번
b = input("숫자를 입력하세요 : ")
if(int(b) % 2 == 0):
    print("짝수입니다")
else:
    print("홀수입니다")

# 114번
c = int(input("숫자를 입력하세요 : "))
if(c+ 20 >255):
    print(255)
else:
    print(c+20)
    
# 115번
if(c-20 < 0):
    print(0)
elif(c-20 > 255):
    print(255)
else:
    print(c-20)
    
# 116번
time = input("현재 시간 : ")
if time[-2:] == "00":
    print("정각 입니다")
else:
    print("정각이 아닙니다.")

# 117번
fruit = ["사과", "포도", "홍시"]
ask_f = input("좋아하는 과일은? ")
if ask_f in fruit:
    print("정답입니다")
else:
    print("목록에 없습니다.")

# 118번
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
ask_I = input("종목명을 입력 : ")
if ask_I in warn_investment_list:
    print("투자 경고 종목입니다.")
else:
    print("투자 경고 종목이 아닙니다.")
    
# 119번
fruit2 = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
ask_ff = input("제가 좋아하는 계절은 : ")
if ask_ff in fruit2:
    print("정답입니다.")
else:
    print("오답입니다.")

# 120번
ask_ad = input("제가 좋아하는 과일은 : ")
if ask_ad in fruit2.values():
    print("정답입니다.")
else:
    print("오답입니다.")
    