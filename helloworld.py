import math
import os
import sys

import requests

print (sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


r = requests.get("https://coreyms.com")
print(r.status_code)


""" def AddTwoNumbers(x, y):
    return x + y

def main():
    sum = AddTwoNumbers(5,9)
    print(sum)
main() """
