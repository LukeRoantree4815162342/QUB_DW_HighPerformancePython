## What's a CLI?

A 'CLI' is a 'Command Line Interface' for a program/tool. They're commonly used by programmers who enjoy working from a terminal (or don't enjoy it but need to anyway), and are much easier to build than graphical user interfaces (GUIs) or web-apps. As they're much easier to build, they're often used for prototyping tools/ideas in order to get the main bulk processing and such figured out before worrying about how it should look to a user. 
---

## What CLI programs might I have used before?

If you use a version of Linux, you'll almost certainly have used some in the terminal - most common shell commands are technically CLI interfaces to programs, e.g. 'grep' for searching a file for keywords / regular expressions, or 'wc' for counting lines, words, and characters in a file. In the last example here, we make 'python\_wc' - a python implementation of the wc tool. Other than a few small differences when given unusual input (and processing speed for large files), it should be roughly interchangeable for the standard wc command.

--------------------------------------------------------------------------------------------

## Examples Order:
> first.py

> second.py

> third.py

> python\_wc

![QUB Logo](https://blogs.qub.ac.uk/footnotesqub/files/2015/03/QUBLogo.gif)

## I want to make CLIs but sys/argparse are too bare-bones, what should I do?

There're other libraries and frameworks for making CLIs in Python, for example
[Click](https://click.palletsprojects.com/en/7.x/) which is installable with 
pip, and is easy to get started with. I have used it and would recommend it.

Another option is [Fire](https://github.com/google/python-fire), made by Google,
which focuses on taking as little effort as possible to give a python program a
command line interface, and is also available for installation on pip, and on conda.
I haven't yet used this one, although from scanning their examples, it looks nice.
