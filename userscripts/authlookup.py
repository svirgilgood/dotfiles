#!/usr/bin/env python3

import os
import urllib.parse as uri_encode


def main():
    text = os.environ['QUTE_SELECTED_TEXT']
    url = "http://nova.atla.com/admin/workbench/search?product=&type=authority&query=%s&heading=&series=&author=&subject=&class=&lang=&keydate=&id_type=&value=&ed_state=&image=&acqu=&assignee_uid=&x=&x_past=&uid=&created%5Bgte%5D=&created%5Blte%5D=&vid_uid=&changed%5Bgte%5D=&changed%5Blte%5D=".replace('%s', uri_encode.quote(text))
    with open(os.environ['QUTE_FIFO'], 'w') as fifo:
        fifo.write("open -t %s" % url)
    


if __name__ == '__main__':
    main()
