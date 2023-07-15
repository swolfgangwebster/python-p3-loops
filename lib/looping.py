#!/usr/bin/env python3

def happy_new_year():
    n=10
    while (n > 0):
        print(n)
        n = n - 1
    print("Happy New Year!")
    # code goes here!
    pass

def square_integers(int_list):
    # code goes here!
    return [x*x for x in int_list]
    pass

def fb(n):
    if (n%3==0 and n%5==0):
        return "FizzBuzz"
    if(n%3==0):
        return "Fizz"
    if(n%5==0):
        return "Buzz"
    return n

def fizzbuzz():
    # code goes here!
    for n in range(1, 1+ 100):
        print(fb(n))
    pass
