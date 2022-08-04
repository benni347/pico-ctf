#!/usr/bin/env python3

import sys
import os

# Get the current working 
# directory (CWD)
cwd = os.getcwd()

file = "cat.jpg"

loc = cwd + "/" + file

try:
    f = open(file, "r")
    text = f.read()
    f.close()
expect IOError:
    print("Error")
print(text)
