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
    
    def clean(self):
        os.chdir(self.root)
        os.system(f'git filter-repo --path-regex {match} --force')
        

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
