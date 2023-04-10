# 131번
과일 = ["사과", "귤", "수박"]           #한글 지원이 돼??
for 변수 in 과일:
    print(변수)                     #과일 리스트 내의 요소 출력

# 132번
과일 = ["사과", "귤", "수박"]
for 변수 in 과일:
  print("#####")                   # "####" 3줄 출력

# 133번, 134번
for 변수 in ["A", "B", "C"]:
    print(변수)
      
print("출력 : ", "A")
print("출력 : ", "B")
print("출력 : ", "C")

# 135번
for 변수 in ["A", "B", "C"]:
    b = 변수.lower()
    print("변환:", b)
    
a = ["A", "B", "C"]
print("변환 :", a[0].lower())
print("변환 :", a[1].lower())
print("변환 :", a[2].lower())

# 136번, 137번
for num in [10, 20, 30]:
    print(num)

# 138번
for num in [10, 20, 30]:
    print(num)
    print("-------")

# 139번
print("++++")
for num in [10, 20, 30]:
    print(num)

# 140번
for num in range(4):
    print("-------")
