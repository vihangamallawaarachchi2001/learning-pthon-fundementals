lower_boundary = 1500
upper_boundary = 2700

def returnNumbersDivisableBySevenAndMultiplyableByFive():
    results =[]
    for number in range(lower_boundary, upper_boundary + 1):
        if number % 7 == 0 and number % 5 == 0:
            results.append(number)
        
    return results
       
        
print(returnNumbersDivisableBySevenAndMultiplyableByFive())