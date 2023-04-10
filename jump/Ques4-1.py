def avg_numbers(*args):             #입력 무한
    result = 0
    for i in args:
        result += i
    print(result / len(args))
    return result / len(args)

avg_numbers(1,2)
avg_numbers(1,2,3,4,5)