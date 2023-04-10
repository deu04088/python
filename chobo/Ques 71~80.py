#71번
my_variable = ()
print(type(my_variable))

#72번
movie_rank = ("닥터 스트레인지", "스플릿", "럭키")
print(movie_rank)                   #튜플, 리스트 지정 방식은 괄호 모양

#73번
tup = (1, )
print(type(tup))

#74번
#t = (1, 2, 3)
#t[0] = 'a'           튜블은 변경 불가능

#75번
t = 1, 2, 3, 4
print(type(t))                      #?????? 괄호없어도 된다함

#76번
t1 = ('a', 'b', 'c')
t1 = ('A', 'b', 'c')                #튜플은 재정의 해야 함
print(t1)

#77번
interest = ('삼성전자', 'LG전자', 'SK Hynix')
li1 = list(interest)
print(type(li1))

#78번
interest1 = ['삼성전자', 'LG전자', 'SK Hynix']
tup1 = tuple(interest1)            #튜플화하는데에 띄어쓰기도 없어야 함
print(type(tup1))

#79번
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)                  #a,b,c 각각 들어가나 봄

#80번
num = tuple(range(2, 100, 2))
print(num)