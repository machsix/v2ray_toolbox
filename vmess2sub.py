#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json
import argparse
import base64

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='generate html file from v2rayN configuration file')

    parser.add_argument('CONF', help='v2rayN configration file')
    parser.add_argument('OUTPUT', help='HTML file for subscription')
    parser.add_argument('-l', '--link', default='STDOUT', help='file to store vmess links (default: STDOUT)')

    ARGS = parser.parse_args()
    with open(ARGS.CONF, 'r') as f:
        conf = json.load(f)

    link = ['vmess://' + base64.urlsafe_b64encode(json.dumps(i).encode('utf-8')).decode() for i in conf]
    text = '\n'.join(link)
    html = base64.urlsafe_b64encode(text.encode('utf-8')).decode()

    with open(ARGS.OUTPUT, 'w', encoding='utf-8') as f:
        f.write(html)

    if ARGS.link == 'STDOUT':
        for i in link:
            print(i + '\n')
    else:
        with open(ARGS.link, 'w', encoding='utf-8') as f:
            for i in link:
                f.write(i + '\n')
