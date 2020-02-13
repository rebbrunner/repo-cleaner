import os
import re
import subprocess
from settings import *

# Get list of files
file_list = []
for subdir, dirs, files in os.walk(ROOT_DIR):
    for file in files:
        file_list.append(file)

# Get list of files not matching
names = [file for file in file_list if not re.match(MATCH, file)]

# Call git command on files
for name in names:
    os.system(f'git filter-branch --tree-filter "git rm {name} -f" -f')
os.system('git reflog expire --expire-unreachable=now --all')
os.system('git gc --aggressive --prune=now')