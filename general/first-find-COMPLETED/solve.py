#!/usr/bin/env python3
"""
This file will find in the current cwd, and also every subfolder, every .txt.
It finds the files using regex. It will also output the file content and use regex to find the picoCTF{} str.
:Autor: benni347@github.com
"""
import os
import re

regex = r".*\.txt\n"

file_list = ""
rootdir = os.getcwd()
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        file_list += os.path.join(subdir, file) + "\n"
        
        #print(os.path.join(subdir, file))

matches = re.finditer(regex, file_list, re.MULTILINE)
file_contents = ""

for matchNum, match in enumerate(matches, start=1):
    
    #print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    #for groupNum in range(0, len(match.groups())):
    #    groupNum = groupNum + 1
    #    
    #    print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))
    #file_contents += 
    m = match.group()
    m = m.strip()
    f = open(m, "r")
    file_contents += f.read()
    f.close()

regex_pico = r"picoCTF{.*}"
matches_pico = re.finditer(regex_pico, file_contents, re.MULTILINE)

for matchNum, match in enumerate(matches_pico, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
