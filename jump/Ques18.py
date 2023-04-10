import re
p = re.compile("[a-z]+")        #문자열 컴파일
m = p.search("5 python")        #문자열만 탐색
print(m.start() + m.end())      #문자열 시작과 끝