numbers = [1, 2, 3, 4, 5]
result =[]

for n in numbers:
    if n % 2 == 1:
        result.append(n*2)
        
        
print(result)

result =[n*2 for n in numbers if n % 2 ==1]
print(result)
