#!/usr/bin/env python3
'''
For creating an Engineering notebook, see http://dankleiman.com/2018/01/28/keeping-an-engineering-notebook/ 
This script expects a environmental variable "NOTEPATH", set that in the
.zshenv or equivalent
'''

import os
import argparse
import sys


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-n', '--notepath', help="Set the path to the notbooks directory")
    ap.add_argument('-d', '--description', help="Add a description")
    ap.add_argument('-l', '--list', help="List all of the Notebook projects in NOTEPATH", action='store_true')
    ap.add_argument('-p', '--papers', help='Use the Paper\'s directory', action='store_true')
    ap.add_argument('term', nargs='?')
    
    a = ap.parse_args()
    #term = '_'.join(a.term)
    if a.list:
        projects = os.listdir(os.environ['NOTEPATH'])
        projects.sort()
        for p in projects:
            print(p)
        sys.exit()
    if a.notepath:
        notepath = a.notepath
    elif a.papers:
        notepath = os.environ['PAPERS']
    else:
        notepath = os.environ['NOTEPATH']

    description = a.description
    if not a.description:
        description = "hello world"
    term = a.term 
    if not a.term:
        term = input('What is the name of your project?\n')
    
    os.chdir(notepath)
    os.mkdir(term)
    os.chdir(term)
    os.mkdir('notes')
    os.mkdir('data')
    os.mkdir('scripts')
    readme = open('README.md', 'w')
    string = "# %s \n\n%s" % (term, description)
    readme.write(string)
    readme.close()



if __name__ == '__main__':
    main()
