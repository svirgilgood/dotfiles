#!/usr/bin/env python3

import clipboard 
import urllib.parse
import os 


def main():
    text = clipboard.paste().replace('-\n', '')
    text = text.replace('\n', '')
    text = urllib.parse.quote(text) 
    url = 'https://translate.google.com/#auto/en/' + text
    with open(os.environ['QUTE_FIFO'], 'w') as fifo:
        fifo.write("open %s" % url)



if __name__ == '__main__':
    main()
