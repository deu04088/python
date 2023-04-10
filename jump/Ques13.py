def Dashinsert(a):
    list = []
    for i in a:
        list.append(i)
        
        
    re = []
    for i in list:
        list = int(list)
        re.append(i)
        if list[i]%2 == 0 and list[i+1]%2 == 0:
           re.append('*')
        if list[i]%2 == 1 and list[i+1]%2 == 1:
           re.append('-') 
    
    print(re)
    
Dashinsert('4546793')
