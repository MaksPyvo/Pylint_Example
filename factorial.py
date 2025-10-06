# factorial.py

import time

final_list = []
# Function to calculate factorial
def factorial(n):
    """
    Calculate factorial of n.
    :param n: integer
    :return: n!"""
    time.sleep(.1)

    result = 1

    for i in range(1, n+1):
        result = result * i

    return result

# Function to calculate sum of factorials
def sum_factorial():
    """
    Calculate sum of factorials from 0 to 49.
    :return: sum of factorials
    """
    for i in range(50):

        final_list.append(factorial(i))

    result = sum(final_list)

    print("Final SUM = {}".format(result))

    return result
if __name__ == "__main__":

    sum_factorial()
