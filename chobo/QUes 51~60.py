#51번
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
print(movie_rank)

#52번
movie_rank.append("배트맨")
print(movie_rank)

#53번
movie_rank.insert(1, "슈퍼맨")
print(movie_rank)

#54번
del movie_rank[3]
print(movie_rank)

#55번
del movie_rank[3]
del movie_rank[2]               #range가 자동으로 줄어들긴 함
print(movie_rank)

#56번
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print(langs)

#57번
nums = [1, 2, 3, 4, 5, 6, 7]
ma = max(nums)
mi = min(nums)
print(ma, mi)

#58번
nums = [1, 2, 3, 4, 5]
print(sum(nums))

#59번
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))

#60번
nums = [1, 2, 3, 4, 5]
aver = sum(nums) / len(nums)
print(aver)
