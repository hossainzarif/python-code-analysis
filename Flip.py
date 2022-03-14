from itertools import combinations
from sys import settrace
import snoop

def my_tracer(frame, event, arg = None):
    # extracts frame code
    code = frame.f_code

    # extracts calling function name
    func_name = code.co_name

    # extracts the line number
    line_no = frame.f_lineno

    print(f"A {event} encountered in \
    {func_name}() at line number {line_no} ")

    return my_tracer
  
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
def is_prime(num):
    num = num+1
    flag = False
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                break
    if flag:
        return False
    else:
        return True
def remainder (num1,num2):
    return num1/num2
def division (num1,num2):
    return num1%num2
# @snoop
def divide_num(numlist):
    for comb in combinations(numlist,2):
        num1,num2 = comb
        if(is_prime(num1) or is_prime(num2) ):
          rem =  remainder(num1,num2)
          print(f"{num1} divided by {num2} is equal to {rem}")

        else:
            val= recur_fibo(num1)
            res = division(val,num2)
            print(f"{val} divided by {num2} is equal to {res}")


settrace(my_tracer)
num_list = [12,11,14]
divide_num(num_list)
settrace(None)
