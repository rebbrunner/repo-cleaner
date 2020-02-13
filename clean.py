import os
import re
import argparse

'''Cleaner
Cleans a repo of unwanted files - useful for getting rid of large binary files
Arguments: root -> string: The root you want to run cleaner in (Works in working directory or .git directory)
           match -> string: regex expression of what you want to KEEP
Returns  : Repository cleaned of unwanted blobs
'''
class Cleaner:
    def __init__(self, root, match):
        self.root = root
        self.match = match
        self.file_list = []
        self.names = []

    # Get list of files
    def get_files(self):
        file_list = []
        for subdir, dirs, files in os.walk(self.root):
            dirs[:] = [d for d in dirs if d not in '.git']
            for file in files:
                self.file_list.append(file)

    # Get list of files not matching
    def get_names(self):
        self.names = [file for file in self.file_list if not re.match(self.match, file)]

    # Call git command on files
    def run_git(self):
        os.chdir(self.root)
        for name in self.names:
            os.system(f'git filter-branch --tree-filter "git rm {name} -f" -f')
        os.system('git reflog expire --expire-unreachable=now --all')
        os.system('git gc --aggressive --prune=now')
    
    def clean(self):
        self.get_files()
        self.get_names()
        self.run_git()

# Test drive code
# Uncomment code below to test
# parser = argparse.ArgumentParser()
# parser.add_argument('root')
# parser.add_argument('match')
# args = parser.parse_args()
# root = args.root
# match = args.match

# cleaner = Cleaner(root, match)
# cleaner.clean()
