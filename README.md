# QUB Development Weeks: High Performance Python
Code and more for the QUB Development Weeks event 'High Performance Python'

---
## Getting Started:

1) Check if Anaconda is installed - this isn't essential in general for using Python, as there is other ways to set up and use Python, but 
to avoid runing into versioning problems between different Python / library distributions I'm standardising this course with conda
environments.

This means you'll be installing the same version of Python as I'm using as I give this course, as well as the same
versions of the same external packages that I use - in a temporary virtual environment that won't mess up any other Python installs you have.

To check if anaconda is installed properly, open a terminal (Windows - search Command Prompt or git-bash, MacOS - search terminal, linux - you know how)

In the terminal run "conda list". If you get a list of packages, or even anything other than "no command found" or similar - you're all good! 

Close the terminal now.

2) If not already installed, download and install [Anaconda](https://www.anaconda.com/distribution/)

3) At this point I'll assume I've shown you how to download / clone this repository (or you already knew how and did it yourself). Open a terminal
in this directory (where this repository is):

> Windows - in file manager, navigate to this repo, right click anywhere and click 'command prompt here'

> MacOS - in Finder, navigate to this repo, then (top left of screen) click 'Finder'-\>Services-\>'new Terminal at Folder'

> Linux - cd to this repo

and run "conda create  --name qubcourse  --file conda\_package\_list.txt python=3.7.5", which will create a new virtual environment, with a specific version of Python,
and will install the same versions of the same packages I had installed when I made this course.

This will take a while, so I'll probably have started going through the earlier parts of the course during these downloading and installing.

4) In your terminal, run "conda activate qubcourse". This tells it to use the virtual environment we made a minute ago. When we're done, we can run "conda deactivate"
to go back to the way things were before. 

5) In your terminal, still in this directory, run "jupyter notebook" - this should cause a webpage to open, with a list of what's in this directory. To start with,
click on the 'PythonRefresher.ipynb' link.


That's us fully set up and started!

---

*Note: In 2019 split into 'Python Refresher Course' (winter) and 'High Performance Python' (summer) due to length of additional content*

### Stable: [Python Refresher](PythonRefresher.ipynb)

### Unstable / Untidy: [High Performance Sections (mostly tidy enough)](HighPerformance)
---------------------------------------------------------------------------------------------

# 2019 Updates Now Out

--------------------------------------------------------------------------------------------

## Python Refresher Course Overview:
> Commenting

> Basic Data Types

> Conditional Logic & Basic Loops

> Comprehensions

> Functions & Lambdas

> Intro to OOP Python

> Generators & Iterators

> Handling Files

> Numpy & Scipy

> Pandas

> Matplotlib

> Scikit-Learn

> Free External Resources (IDEs, Books, Library / Domain-Specific Tutorials, List of Useful Libraries)


![QUB Logo](https://blogs.qub.ac.uk/footnotesqub/files/2015/03/QUBLogo.gif)



**Team Members**

| First Name    | Last Name     | 2018 | 2019 |
| ------------- |:-------------:|:----:|:----:|
| Conor         | Duffy         |   Y  |   N  |
| Silas         | O'Toole       |   Y  |   N  |
| Luke          | Roantree      |   Y  |   Y  |

Special thanks to:


* Dr. Garbriele De Chiara - for helping organise the event and booking the computer suites


* Victoria Coulter - for obtaining funding, setting up the registration, and more




--------------------------------------------------------
## **What This Doesn't Cover:**

### Python Refresher:

> Interacting with computer via os and sys (2019 Updates touch on some)


> Installing extra libraries


> Machine learning libraries other than Sklearn

-------------------------------------------------------
## High Performance Python summer-2019 release updates to include:
> Multi-Threading


> Parallel Processing (joblib and mpi4py)


> Cython other than via Jupyter Notebook


> Pythran


> f2py
