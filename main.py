from itertools import combinations
from loguru import logger

def division(num1: int, num2: int):
   return num1 / num2

@logger.catch
def divide_numbers(num_list: list):
   for comb in combinations(num_list, 2):
       num1, num2 = comb
       print(f"{num1} divided by {num2}.")
       res = division(num1, num2)
       print(f"{num1} divided by {num2} is equal to {res}.")

if __name__ == '__main__':
   num_list = [ 2, 1, 0]
   divide_numbers(num_list)


def calc_total(days):
    total = 40 * days
    if days >= 7:
        total = total - 50
    elif days >= 3:
        total = total - 20
    return total