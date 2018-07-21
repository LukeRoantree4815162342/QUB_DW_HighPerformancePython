#!/usr/bin/env/python

import sys

"""
Internally, sys.argv is used by all cli building tools to access the arguments passed
when calling the CLI program. 

This example shows how to use it directly.

As shown below, the first element of sys.argv is the command used (python program called),
and the remaining ones are the extra arguments passed to the script
"""

command = sys.argv[0]
arg1 = sys.argv[1]
arg2 = sys.argv[2]


print('the command {} was used, with the arguments {} and {}'.format(command,arg1,arg2))


