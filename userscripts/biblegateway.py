#!/usr/bin/env python3
from urllib import parse
import os
import sys

base_url = 'https://www.biblegateway.com/passage/?'


def main():
    parts = sys.argv[1:]
    with open(os.environ['QUTE_FIFO'], 'w') as fifo:
        if len(parts) == 2:
            fifo.write("open -t {}search={}".format(base_url, parse.quote(' '.join(parts))))
            sys.exit()
        search = parse.quote(' '.join(parts[:2]))
        version = parse.quote(parts[2])
        fifo.write("open -t {}search={}&version={}".format(base_url, search, version))
    

if __name__ == '__main__':
    main()
