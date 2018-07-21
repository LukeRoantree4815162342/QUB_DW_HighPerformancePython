#!/usr/bin/env/python

import argparse

"""
argparse allows you to do a lot of extra logic with input
arguments - such as treating arguments as flags, making
arguments mutually exclusive, count how many times an 
argument is specified, and more. This example will show
a few common usages of these more specialised options
"""

parser = argparse.ArgumentParser()

parser.add_argument('num1',type=float, help='first number')

group = parser.add_mutually_exclusive_group()
# make a mutually exlusive group - only one parameter may
# be specified from the ones we add here

group.add_argument('--multiply','-m', help='multiply num1 by num2', action='store_true')
# the action='store_true' part tells the program that this 
# argument won't be given a value in the command line, but
# if it is present, assign it a value of True

group.add_argument('--divide','-d', help='divide num1 by num2', action='store_true')
group.add_argument('--subtract','-s', help='subtract num1 from num2', action='store_true')
group.add_argument('--add','-a', help='add num1 to num2', action='store_true')

parser.add_argument('num2',type=float, help='second number')

parser.add_argument('--sigfigs', '-f', help='how many significant figures to display [-f = 1, -fff = 3]', action='count')

args = parser.parse_args()

if not args.sigfigs:
    sf = 5
else:
    sf = args.sigfigs

if args.multiply:
    print("{0:.{1}g}".format(args.num1*args.num2,sf))
    # string formatting; second argument specifying number
    # of sig figs to display for the first argument
if args.divide:
    print("{0:.{1}g}".format(args.num1/args.num2,sf))
if args.subtract:
    print("{0:.{1}g}".format(args.num1-args.num2,sf))
if args.add:
    print("{0:.{1}g}".format(args.num1+args.num2,sf))



