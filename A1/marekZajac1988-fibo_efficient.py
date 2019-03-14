#!/usr/bin/python3.6

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("input", type=int,
                    help="input integer to calculate nth number of fibonacci sequence")
parser.add_argument("-a", "--all", action="store_true",
                    help="output all numbers of fibonacci sequence up to input")
parser.add_argument("-n", action="store_true",
                    help="output only nth number of fibonacci sequence")
args = parser.parse_args()

def fibonacci(n):
    fibonacci_list = []
    a, b = 0, 1
    for i in range(0,n):
        a, b = b, a + b
        fibonacci_list.append(a)
    print(fibonacci_list[n-1])

def fibonacciAll(n):
    fibonacci_list = []
    a, b = 0, 1
    for i in range(0,n):
        a, b = b, a + b
        fibonacci_list.append(a)
    print(", ".join(map(str,fibonacci_list)))


if args.n:
    fibonacci(args.input)

if args.all:
    fibonacciAll(args.input)
