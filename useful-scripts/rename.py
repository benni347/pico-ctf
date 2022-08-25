#!/usr/bin/env python3
import os
cwd = os.getcwd()
new_dir_name = cwd + "-COMPLETED"
os.rename(cwd, new_dir_name)
