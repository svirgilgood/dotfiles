#!/usr/bin/env python3

import clipboard
import os

def main():
    url = os.environ['QUTE_URL']
    node = url.split('/').pop()
    clipboard.copy(node)


if __name__ == '__main__':
    main()
