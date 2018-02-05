#!/usr/bin/env python3

import os
import argparse


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-n', '--notepath', help="Set the path to the notbooks directory")
    ap.add_argument('-d', '--description', help="Add a description")
    ap.add_argument('term', nargs='*')
    
    a = ap.parse_args()
    term = '_'.join(a.term)
    if a.notepath:
        notepath = a.notepath
    else:
        notepath = os.environ['NOTEPATH']

    if not a.term:
        term = input('What is this project names? ')
    description = a.description
    if not a.description:
        description = "hello world"
    
    os.chdir(notepath)
    os.mkdir(term)
    os.chdir(term)
    os.mkdir('notes')
    os.mkdir('data')
    os.mkdir('scripts')
    readme = open('README.md', 'w')
    string = "# %s \n\n %s" % (term, description)
    readme.write(string)
    readme.close()



if __name__ == '__main__':
    main()
