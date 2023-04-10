# 81번                  ???????
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, _, _= scores              #답지 보고도 이해불가
print(valid_score)

# 82번
a, b, *valid_score = scores
print(valid_score)

# 83번
a, *valid_score, b = scores
print(valid_score)                  #딕셔너리 개념 작살남 다시 공부

# 84번
temp = { }

# 85번
icecream = {"메로나": 1000, "폴라포": 1200, "빵빠레": 1800}
print(icecream)

# 86번
icecream["죠스바"] = 1200
icecream["월드콘"] = 1500
print(icecream)

# 87번
print("메로나 가격: ", icecream["메로나"])

# 88번
icecream["메로나"] = 1300
print(icecream)

# 89번
del icecream["메로나"]
print(icecream)

# 90번
#icecream1 = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
#icecream1['누가바']
# => 누가바가 없음
