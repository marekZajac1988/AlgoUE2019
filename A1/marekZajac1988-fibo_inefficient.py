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

def fibonacciRecursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fibonacciRecursive(n-1)+fibonacciRecursive(n-2))

if args.n:
    print(fibonacciRecursive(args.input))

if args.all:
    for i in range(0,args.input):
        print(fibonacciRecursive(i), end=", ")
    print()