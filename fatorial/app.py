def cal_factorial(n):
    if n <0:
        return "need a non negative number"
    output=1
    for i in range(1, n+1, +1):
        output = output * i
    return output

print(cal_factorial(5))