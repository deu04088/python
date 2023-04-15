def Dashinsert(a):
    list = []
    for i in a:
        list.append(int(i))
        
    re = []
    for i in range(len(list)):
        re.append(list[i])
        if i < len(list)-1:
            if list[i]%2 == 0 and list[i+1]%2 == 0:
                re.append('*')
            if list[i]%2 == 1 and list[i+1]%2 == 1:
                re.append('-') 
    
    result = ''
    for i in re:
        if type(i) is int:
            result += str(i)
        else:
            result += i
    print(result)
    
Dashinsert('4546793')
