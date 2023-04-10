result = 0
try:
    [1, 2, 3][3]
    "a"+1
    4 / 0
except TypeError:
    result += 1
except ZeroDivisionError:
    result += 2
except IndexError:
    result += 3
finally:
    result += 4
    
print(result)

# try문 첫 줄에서 인덱스 오류가 발생하여 10번째 줄부터 코드가 실행된다
# 따라서 3 + 4의 결과 7이 출력된다