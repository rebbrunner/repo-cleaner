# Repo Cleaning Script

Author: Rebecca Brunner
<br>
Date: 13 February 2020

## Description

Script that cleans repositories of binary files

## Requirements

- git-filter-repo (https://github.com/newren/git-filter-repo) must be installed to path
- python 3.6+

## Architecture

    --> clean.py    = Main file
    --> test        = Test git directory to run script on
    --> test - Copy = Backup of test folder.  Replace after testing script
