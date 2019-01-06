#!/usr/bin/python3

# The shebang (above) is used to tell the computer what to use to run the program
# when it is made executable. This may change slightly depending on operating system

import argparse, time

"""
An easier way of making CLI apps is to use the 'argparse' module (part of the stdlib).

It lets you easily specify and name arguments, and also automatically builds a --help
usage guide based on the argument specifications.

Additionally, each argument can be given a description with the 'help' parameter,
a type to be interpreted as (default is string), and a default can be given (optional
arguments only).
"""

parser = argparse.ArgumentParser() 
# Create a parser object

parser.add_argument('person') 
# all parameters after the name are optional.

parser.add_argument('note', help='enter a note', type=str) 
# you can specify types and help

parser.add_argument('--delay', '-d', help='enter a delay in seconds', type=int, default=5)
# arguments are made optional by starting the name with --, and can be given a shorter alias
# immediately after, starting with a single -.
# optional arguments can be given a default value.

args = parser.parse_args()

time.sleep(args.delay)
print('{}: {}'.format(args.person, args.note))


