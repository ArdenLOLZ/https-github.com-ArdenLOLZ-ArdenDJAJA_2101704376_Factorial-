import math
def calculator(num1,num2,operator,taip):
    if operator == '+':
        ans = num1/num2
    elif operator == '-':
        ans = num1/num2
    elif operator == '*':
        ans = num1/num2
    elif operator == '/':
        ans = num1/num2
    else:
        print('operator is invalid')
    if taip =='1':
        return float(ans)
    if taip == '2':
        return int(ans)

num1 = input()
num2 = input()
operator = input('input operator \n ')
taip = input('float(1) or integer(2)\n ')
print(calculator(int(num1),int(num2),operator,taip))

